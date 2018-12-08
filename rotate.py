#add completion of rotation variable and return it
import RPi.GPIO as GPIO
import time
GPIO.setup(6,GPIO.OUT)
print "LED on"
GPIO.output(6,GPIO.HIGH)
time.sleep(3)
print "LED off"
GPIO.output(6,GPIO.LOW)
