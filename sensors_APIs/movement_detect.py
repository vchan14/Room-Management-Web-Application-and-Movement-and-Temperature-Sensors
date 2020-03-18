import RPi.GPIO as GPIO
import time
import sys
import lcd_16x2 

sys.path.append('./../database')
GPIO.setmode(GPIO.BCM)
from database import UpdateDB


class ULTRASONIC_SENSOR():
    def __init__(self, trig_gpio, echo_gpio):
        self.trig = trig_gpio
        self.echo = echo_gpio
        # set trig for output
        # set echo for ipnut
        GPIO.setup(trig_gpio, GPIO.OUT)
        GPIO.setup(echo_gpio, GPIO.IN)

    def calculateDistance(self, pulse_end, pulse_start):
        # we know that sound's speed is 34,000cm/s
        # distance = time_taken *  34,000 / 2
        # divide by two because the sound needs to travel back and forth

        return ((pulse_end - pulse_start) * 17150)

    def detect(self):
        current_dist = self.distance()
        if(current_dist < 50):
            return True
        else:
            return False

    def distance(self):
        time.sleep(0.01)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        pulse_start = 0
        pulse_end = 0

        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()

        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        return self.calculateDistance(pulse_end, pulse_start)


# assign GPIO

TRIG_A = 23
ECHO_A = 24

TRIG_B = 22
ECHO_B = 27

sensor_A = ULTRASONIC_SENSOR(TRIG_A, ECHO_A)
sensor_B = ULTRASONIC_SENSOR(TRIG_B, ECHO_B)

try:
    time_diff = 0
    time_A = 0
    time_B = 0
    obj = UpdateDB()

    while(True):
        
        if(sensor_A.detect() == True):
            print("A is detected");
            time_A = time.time()
            while(1):
                if(sensor_B.detect() == True):
                    print("B is detected")
                    print("Going in")
                    obj.incrementNumberStudent("14-237")
                    lcd_16x2.lcd_string("Num of student:", lcd_16x2.LCD_LINE_1)
					lcd_16x2.lcd_string(str(num_student), lcd_16x2.LCD_LINE_2)

                    time.sleep(0.8)
                    break
                else:
                    time_diff = time.time() - time_A
                    if(time_diff > 5):
                        break
        if(sensor_B.detect() == True):
            print("B is detected")
            time_B = time.time()
            while(1):
                if(sensor_A.detect() == True):
                    print("A is detected")
                    print("Going out")
                    obj.decrementNumberStudent("14-237")
                    lcd_16x2.lcd_string("Num of student:", lcd_16x2.LCD_LINE_1)
					lcd_16x2.lcd_string(str(num_student), lcd_16x2.LCD_LINE_2)
                    time.sleep(0.8)
                    break
                else:
                    time_diff = time.time() - time_B
                    if(time_diff > 5):
                        break
        
# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()
