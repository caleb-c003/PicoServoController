# Code for use with boot.py and MPU6050.py on pico
# Code for reading (GY-521) MPU6050 Accelerometer/Gyro Module 
# and outputting x and y to serial.

from MPU6050 import MPU6050
import time
from machine import Pin
from time import sleep_ms


VCC = Pin(13, Pin.OUT)
GND = Pin(12, Pin.OUT)
VCC.value(1)
GND.value(0)
time.sleep(.2)


mpu = MPU6050()

num_samples = 50
gX_sum = 0
gY_sum = 0
servo_range = 10
xMax_val = 20
yMax_val = 11

# Reads gyro data (misdeclared in module, accel_data is gyro) and converts to values accepted by the servos
while True:
    for i in range(num_samples):
        gyro = mpu.read_accel_data() # read the gyro [ms^-2]
        gX_sum += gyro["x"]
        gY_sum += gyro["y"]
        
    gX_avg = gX_sum/num_samples
    gY_avg = gY_sum/num_samples
    gX_pos = (-1 * gX_avg + 10)*(servo_range/xMax_val)
    gY_pos = (-1 * gY_avg + 6)*(servo_range/yMax_val)
    print(gX_pos, gY_pos)
    time.sleep(0.5)
    gX_sum = 0
    gY_sum = 0
