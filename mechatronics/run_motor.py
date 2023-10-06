from machine import Pin, PWM

"""
Enumeration variables that do not change.
"""
RUN = False
MAX_PWM = 65535
LEFT_FORWARD = 0
LEFT_REVERSE = 1
RIGHT_FORWARD = 0
RIGHT_REVERSE = 1

"""
Declare pin modes for right and left wheel.

The direction pin is used to determined forward or backwards.
The PWM pin is used to determine the speed of the wheel.
"""
r_dir_pin = Pin(0, Pin.OUT)
r_pwm_pin = PWM(Pin(1, Pin.OUT))
l_dir_pin = Pin(2, Pin.OUT)
l_pwm_pin = PWM(Pin(3, Pin.OUT))

"""
Encoder counts and timers for volatile counts.
"""
right_encoder_count = 0
left_encoder_count = 0

"""
Interrupts.

right_encoder_callback is the interrupt for right motor encoder.
left_encoder_callback is the interrupt for the left motor encoder.
interrupt_callback is the interrupt for starting and stopping the motors.
"""
right_enconder_pin = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)
def right_encoder_callback(pin):
    global right_encoder_count 
    right_encoder_count += 1
right_enconder_pin.irq(trigger=Pin.IRQ_FALLING, handler=right_encoder_callback)

left_enconder_pin = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)
def left_encoder_callback(pin):
    global left_encoder_count 
    left_encoder_count += 1
left_enconder_pin.irq(trigger=Pin.IRQ_FALLING, handler=left_encoder_callback)

interrupt_pin = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)
def interrupt_callback(pin):
    global RUN 
    RUN = not RUN
interrupt_pin.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_callback)

"""
Main loop of program.
"""
while True:
    if RUN:
        l_dir_pin.value(LEFT_FORWARD)
        l_pwm_pin.freq(5000)
        l_pwm_pin.duty_u16(MAX_PWM // 6)

        r_dir_pin.value(RIGHT_FORWARD)
        r_pwm_pin.freq(5000)
        r_pwm_pin.duty_u16(MAX_PWM // 6)
    else:
        l_pwm_pin.duty_u16(0)
        r_pwm_pin.duty_u16(0)
