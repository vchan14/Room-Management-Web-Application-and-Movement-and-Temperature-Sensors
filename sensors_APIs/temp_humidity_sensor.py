import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sys

sys.path.append('./../database')
from database import UpdateDB

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)


def getTempHum():
    while True:
        result = instance.read()
        if result.is_valid():
            time.sleep(2)
            return(int(result.temperature), int(result.humidity))


def main():
    obj = UpdateDB()
    while True:
        myTempHum = getTempHum()
        print("Tempearture is {}".format(myTempHum[0]))
        print("Humidity is {}".format(myTempHum[1]))
        obj.updateTemperature("14-237", myTempHum[0])
        obj.updateHum("14-237", myTempHum[1])





if __name__ == '__main__':
    main()
