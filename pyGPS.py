# pyGPS created by Lachlan Page
# Intended for use with GSTAR IV GPS
import serial

class pyGPS:
    """ pyGPS allows for quick use of GSTAR IV gps """

    def __init__(self, baud_rate):
        self.m_serial = serial.Serial('/dev/ttyUSB0', baud_rate, timeout = 5)

        # Members vars related to gps function
        self.latitude = 0
        self.latitude_direction = "NULL"

        self.longitude = 0
        self.longitude_direction = "NULL"

        # UTC time of when fix was taken
        self.fix_time = 0

        self.status_code = 0

        self.num_satellites = 0

        self.horizontal_dilation = 0

        self.mean_altitude = 0

    """ updates the GPS data by reading serial and sets members """
    def updateData(self):
        data_line = self.m_serial.readline()
        data = data_line.split(",")

        # returns lots of satellite data, we only care about GPGGA for the moment
        # First 2/3 decimal places of lat/long correspond to the actual lat/long
        # the rest of digits corespond to the degrees
        # 4807.038 -> 48 . 0703 degrees
        # South direction corresponds to a negative lat/long

        # Status code is a enum of 1 to 8 representing signal fix quality
        if(data[0] == "$GPGGA"):

            self.fix_time = data[1]

            self.latitude = float(data[2])
            self.latitude = self.latitude / 100
            self.latitude_direction = data[3]

            if(self.latitude_direction == "S"):
                self.latitude = -self.latitude

            self.longitude = float(data[4])
            self.longitude = self.longitude / 100
            self.longitude_direction = data[5]

            if(self.longitude_direction == "S"):
                self.longitude = -self.self.longitude

            self.status_code = data[6]

            self.num_satellites = data[7]

            self.horizontal_dilation = data[8]

            self.mean_altitude = data[9]

        # Slows down GPS updating but handles lock on during startup
        else:
            self.updateData()

    """ Pretty print of basic satellite data """
    def printData(self):
        print("Data Recieved: ")
        print("Status Code: {}".format(self.status_code))
        print("Lat: {}".format(self.latitude))
        print("Long: {}".format(self.longitude))
        print("Mean Altitude: {}".format(self.mean_altitude))
        print("Num Satellites: {}".format(self.num_satellites))
        print("Horiz Dilation: {}".format(self.horizontal_dilation))
        print("\n")
        #print(self.latitude, self.longitude, self.status_code)
