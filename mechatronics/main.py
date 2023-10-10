from machine import Pin, PWM, I2C
from drivers.vl53l1x import VL53L1X
from drivers.hcsr04 import HCSR04
import time
"""
Enumeration variables that do not change.
"""
RUN = False
MAX_PWM = 65535
FORWARD = 0
REVERSE = 1

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
Initialize Time of Flight Sensor
"""
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
time_of_flight = VL53L1X(i2c)
tof_distance = time_of_flight.getDistance()

"""
Initialize Ultrasonic Sensor
"""
sensor = HCSR04(trigger_pin=16, echo_pin=17)
distance = sensor.distance_cm()

"""
Driving Commands and Variables
"""
desired_pwm = MAX_PWM // 4
right_output = desired_pwm
left_output = desired_pwm
last_error = 0

def drive(left):
    readSensors()
    if left:
        lComputePD()

    if right_output < 0:
        l_dir_pin.value(FORWARD)
        l_pwm_pin.freq(5000)
        l_pwm_pin.duty_u16(left_output)

        r_dir_pin.value(REVERSE)
        r_pwm_pin.freq(5000)
        r_pwm_pin.duty_u16(right_output)
    elif left_output < 0:
        l_dir_pin.value(REVERSE)
        l_pwm_pin.freq(5000)
        l_pwm_pin.duty_u16(left_output)

        r_dir_pin.value(FORWARD)
        r_pwm_pin.freq(5000)
        r_pwm_pin.duty_u16(right_output)
    else:
        l_dir_pin.value(FORWARD)
        l_pwm_pin.freq(5000)
        l_pwm_pin.duty_u16(left_output)

        r_dir_pin.value(FORWARD)
        r_pwm_pin.freq(5000)
        r_pwm_pin.duty_u16(right_output)


def lComputePD():
    global left_output
    global right_output
    global last_error

    kp = 0.005 * desired_pwm
    kd = 0

    desired_distance = 110
    error = tof_distance - desired_distance
    
    p = kp * error
    i = 0
    d = kd * (error - last_error)
    increment = p + i + d

    left_output = int(desired_pwm - increment)
    right_output = int(desired_pwm + increment)
    constrain()

def readSensors():
    global tof_distance
    tof_distance = time_of_flight.getDistance()

def constrain():
    global left_output
    global right_output

    if left_output > MAX_PWM:
        left_output = MAX_PWM
    elif left_output < -MAX_PWM:
        left_output = -MAX_PWM
    
    if right_output > MAX_PWM:
        right_output = MAX_PWM
    elif right_output < -MAX_PWM:
        right_output = -MAX_PWM

"""
Main loop of program.
"""
while True:
    distance = sensor.distance_cm()
    if distance > 8:
        drive(left=True)
    else:
        print(distance)
        l_pwm_pin.duty_u16(0)
        r_pwm_pin.duty_u16(0)
