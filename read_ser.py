# Code for use with main.py and servo.py on the Raspberry Pi
# Reads line from serial, decodes it and splits it into x and y components

import serial

class Serial:

    def __init__(self, port):
        self.port = serial.Serial(port)

    def readLine(self):
        line = self.port.readline()
        dLine = line.decode('utf-8')
        xypos_list = dLine.strip("b'\r\n")
        xySplit = xypos_list.split(" ")
        xPos = int(xySplit[0].split('.')[0])
        yPos = int(xySplit[1].split('.')[0])
        return xPos, yPos
