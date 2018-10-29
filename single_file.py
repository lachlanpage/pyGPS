# A non object tester version
import serial

ser = serial.Serial('/dev/ttyUSB0', 4800, timeout = 5)

while True:
    line = ser.readline()
    data = line.split(",")

    # returns lots of satellite data, we only care about GPGGA for the moment
    if(data[0] == "$GPGGA"):
        latitude = float(data[2])
        latitude = latitude / 100
        latitude_direction = data[3]

        if(latitude_direction == "S"):
            latitude = -latitude

        longitude = float(data[4])
        longitude = longitude / 100
        longitude_direction = data[5]

        if(longitude_direction == "S"):
            longitude = -longitude

        status = data[6]

        print(latitude, longitude, status)
