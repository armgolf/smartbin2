import RPi.GPIO as GPIO
import time
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
print "LED off"
GPIO.output(18,GPIO.LOW)
