# Simple example use of using pyGPS 
import pyGPS
import time

# Setup pyGPS with a baud rate of 4800
gps = pyGPS.pyGPS(4800)

while True:
    gps.updateData()
    time.sleep(2)
    gps.printData()
