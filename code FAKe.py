"""CircuitPython Essentials Servo continuous rotation servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 0
    time.sleep(2.0)
    my_servo.angle = 180
    time.sleep(2.0)
    
    