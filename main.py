# Use on Raspberry Pi connected to servos and pico.
# Reads gyro numbers from serial connection to pico and feeds the numbers to the servos

import servo
import read_ser

# Initiate servos with pin and data rate
servoX = servo.Servo(18, 50)
servoX.start()
servoY = servo.Servo(16, 50)
servoY.start()

# Open serial connection
ser = read_ser.Serial("/dev/ttyACM0")

# Continuously reads line from serial and decodes it. Outputs numbers to servos.
while True:
    xPos, yPos = ser.readLine()
    servoX.go_to_pos(xPos)
    servoY.go_to_pos(yPos)
