import time
from random import randrange, seed
from machine import Pin, PWM, SPI

from ir_remote_driver import IRRemote
from lcd_display_driver import Display, color565, XglcdFont


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
buzzer = PWM(Pin(9))
buzzer_tones = [131, 165, 196, 262]

# Initialize display
# https://github.com/rdagger/micropython-ili9341
# https://www.youtube.com/watch?v=suCTwxlYgnM
spi = SPI(
    0, 
    baudrate=10000000, 
    polarity=1,
    phase=1,
    bits=8,
    firstbit=SPI.MSB,
    sck=Pin(18), 
    mosi=Pin(19),
    miso=Pin(16)
)
display = Display(spi, dc=Pin(20), cs=Pin(17), rst=Pin(21))
display.clear()

espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)

# Create lists for displaying rectangles
x = 240
y = 320
m = 8
w = (x-3*m) // 2
h = (y-3*m) // 2
colors_display = [color565(255, 0, 0),color565(255, 255, 0),color565(0, 255, 0),color565(0, 0, 255)]
x_coordinates = [(x+m)//2, (x+m)//2, m, m]
y_coordinates =[m, (y+m)//2, (y+m)//2, m]
display.fill_rectangle(0, 0, x, y, color565(255, 0, 255))

# Variable declarations
seed()
sequence_count = 0
sequences = []
current_index = 0
new_game = False
next_round = False

# Set up interrupt button
def interrupt_callback(_):
    global new_game
    new_game = True

interrupt_button = Pin(5, Pin.IN)
interrupt_button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_callback)


def process_move(quadrant):
    display.fill_rectangle(x_coordinates[quadrant], y_coordinates[quadrant], w, h, colors_display[quadrant])
    playtone(buzzer_tones[quadrant], 1000)
    blink_led(led_pins[quadrant], 400)
    time.sleep(.200)
    display.fill_rectangle(0, 0, x, y, color565(255, 0, 255))
    playtone(buzzer_tones[quadrant], 0)


def process_user_selections(action):
    global current_index

    if action == sequences[current_index]:
        current_index+=1
        return True
    else:
        return False


def show_display(screen):
    if screen == "MAIN":
        display.draw_text(80, 80, 'Welcome', espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
        display.draw_text(110, 100, 'to', espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
        display.draw_text(60, 120, 'Simon Says', espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
    elif screen == "NEW_GAME":
        clear_display()
        display.draw_text(70, 100, 'New Game', espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))


def clear_display():
    display.fill_rectangle(0, 0, x, y, color565(255, 0, 255))


def blink_led(pin, time_ms):
    pin.high()
    time.sleep(time_ms/1000)
    pin.low()


def check_state():
    global sequence_count
    global current_index
    global next_round

    if current_index == 20:
        clear_display()
        display.draw_text(70, 100, 'You won!', espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
        while(interrupt_button.value()):
            for pin in led_pins:
                blink_led(pin, 100)
    elif current_index == sequence_count:
        next_round = True
        

def playtone(frequency, volume):
    buzzer.duty_u16(volume)
    buzzer.freq(frequency)


# Only run main loop if this file is directly called
if __name__ == "__main__":
    # Begin main loop
    show_display("MAIN")
    while True:
        # Reset the user action
        user_action = -1

        # Get the last input from IR remote
        last_key_processed = ir_remote.get_last_key_press()

        # Return to main menu when MENU key is pressed
        if last_key_processed == "MENU":
            show_display("MAIN")
        
        # Restart game if new game interrupt is hit
        if new_game:
            # Display New Game screen
            show_display("NEW_GAME")
            time.sleep(1)
            display.fill_rectangle(0, 0, x, y, color565(255, 0, 255))

            # Randomly select the initial sequences
            sequence_count = 4
            for i in range(sequence_count):
                sequences.append(randrange(0, 4))
                process_move(sequences[i])
            
            # Disable new game mode and reset current index
            new_game = False
            current_index = 0
        elif next_round:
            sequence_count += 1
            current_index = 0
            display.draw_text(70, 90, 'Next Round!', espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
            display.draw_text(70, 110, "There are ", espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
            display.draw_text(70, 130, f"{sequence_count} actions", espresso_dolce, color565(255, 255, 255), color565(255, 0, 255))
            time.sleep(2)
            clear_display()
            sequences.append(randrange(0, 4))
            for i in range(sequence_count):
                process_move(sequences[i])
            next_round = False
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
                    # Display the current sequence count to the end user
                    display.draw_text(115, 130, str(current_index), espresso_dolce, 
                                      color565(255, 255, 255), color565(255, 0, 255))
                    # Check to see if a new sequence needs to be made
                    check_state()
                else:
                    display.draw_text(75, 100, "You lose.", espresso_dolce, 
                                      color565(255, 255, 255), color565(255, 0, 255))
                    display.draw_text(70, 120, "Play again?", espresso_dolce, 
                                      color565(255, 255, 255), color565(255, 0, 255))
                    playtone(50, 1000)
                    time.sleep(1)
                    playtone(50, 0)
                    while(interrupt_button.value()): pass
                user_action = -1
