import time
from random import randrange
from machine import Pin, PWM, SPI

from ir_remote import IRRemote
# from ili9341 import Display, color565

# Declare LED pins
red_led = Pin(22, Pin.OUT, value=0)
yellow_led = Pin(26, Pin.OUT, value=0)
green_led = Pin(27, Pin.OUT, value=0)
blue_led = Pin(28, Pin.OUT, value=0)
led_pins = [red_led, yellow_led, green_led, blue_led]

# Declare Button pins
red_button = Pin(10, Pin.IN)
yellow_button = Pin(11, Pin.IN)
green_button = Pin(12, Pin.IN)
blue_button = Pin(13, Pin.IN)
button_pins = [red_button, yellow_button, green_button, blue_button]

# Create IR object
ir_remote = IRRemote(Pin(15, Pin.IN))

# Create Piezo Buzzer
buzzer = Pin(9, Pin.OUT)

# Initialize display
# spi_connection = SPI(
#     0, 
#     baudrate=10000000, 
#     polarity=1,
#     phase=1,
#     bits=8,
#     firstbit=SPI.MSB,
#     sck=Pin(18), 
#     mosi=Pin(19),
#     miso=Pin(16)
# )
# display = Display(spi_connection, dc=Pin(20), cs=Pin(17), rst=Pin(21))
# display.clear()

# Variable declarations
sequence_count = 0
sequences = [-1] * 20
current_index = 0
new_game = False

# Set up interrupt button
def interrupt_callback(_):
    global new_game
    new_game = True

interrupt_button = Pin(5, Pin.IN)
interrupt_button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_callback)


def process_move(quadrant):
    global led_pins
    colors = ["red", "yellow", "green", "blue"]
    blink_led(led_pins[quadrant], 200)
    print(colors[quadrant])
    time.sleep(.500)


def process_user_selections(action):
    global sequences
    global current_index
    if action == sequences[current_index]:
        current_index+=1
        return True
    else:
        return False


def show_display(screen, option_state, keypressed):
    if screen == "MAIN":
        print("Welcome to Simon Says")
    elif screen == "NEW_GAME":
        print("New Game!")


def blink_led(pin, time_ms):
    pin.high()
    time.sleep(time_ms/1000)
    pin.low()


def generate_random_sequence():
    global sequence_count
    global sequences
    for i in range(sequence_count):
        sequences[i] = randrange(0, 4)
        process_move(sequences[i])


def check_win():
    global sequence_count
    global current_index

    if current_index == 8:
        print("You won! Congratulations!")
        while(interrupt_button.value()): pass
    elif current_index == sequence_count:
        sequence_count += 2
        current_index = 0
        generate_random_sequence()

# Only run main loop if this file is directly called
if __name__ == "__main__":
    # Begin main loop
    show_display("MAIN", "", "")
    while True:
        # Reset the user action
        user_action = -1

        # Get the last input from IR remote
        last_key_processed = ir_remote.get_last_key_press()

        # Return to main menu when MENU key is pressed
        if last_key_processed == "MENU":
            show_display("MAIN", "", "")
        
        # Restart game if new game interrupt is hit
        if new_game:
            # Display New Game screen
            show_display("NEW_GAME", "", "")
            time.sleep(1)

            # Set the current number of sequences
            sequence_count = 4

            # Randomly select the initial sequences
            sequence_count = 4
            generate_random_sequence()
            
            # Disable new game mode and reset current index
            new_game = False
            current_index = 0
        else:
            if not button_pins[0].value():
                process_move(0)
                user_action = 0
            elif not button_pins[1].value():
                process_move(1)
                user_action = 1
            elif not button_pins[2].value():
                process_move(2)
                user_action = 2
            elif not button_pins[3].value():
                process_move(3)
                user_action = 3

            # If any button was pressed, then process it
            if user_action > -1:
                # See if the current key pressed is the correct key
                if process_user_selections(user_action):
                    print(current_index)
                    # Check to see if a new sequence needs to be made
                    check_win()
                else:
                    print("You lose. Loser.")
                    while(interrupt_button.value()): pass
                user_action = -1
            
