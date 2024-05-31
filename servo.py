# Code for use with main.py and read_ser.py on the Raspberry Pi
# Creates a servo class with functions for instantiating and controlling servos

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

class Servo:

    def __init__(self, pin, data_rate, lastPos = 0):
        self.pin = pin
        self.data_rate = data_rate
        self.lastPos = lastPos
        GPIO.setup(self.pin, GPIO.OUT) # data pin
        self.pwm =GPIO.PWM(self.pin, self.data_rate)

    # Starts the servo motor
    def start(self):
        self.pwm.start(0)

    # Checks input number is within the servo control range and moves the servo to the givn position
    def go_to_pos(self, pos):
        if pos >= 0 & pos <= 10 & pos != self.lastPos:
            self.lastPos = pos
            new_pos = pos+2
            if new_pos in range(2,13):
                self.pwm.ChangeDutyCycle(new_pos)
                sleep(0.5)

    # Stops servos
    def cleanup(self):
        self.pwm.ChangeDutyCycle(7)
        sleep(1)
        self.pwm.stop()
        GPIO.cleanup()
