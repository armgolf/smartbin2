import time #required for pausing the script
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
import requests
import os
import json
from gpiozero import DistanceSensor

def photo():
    files = (os.listdir("/home/pi/Documents/smartbin2/smartbin2-master/images"))
    #files = (os.listdir("./images"))
    lastfile = files[-1]
    ending = lastfile[6:]
    string = ending[:-4]
    number = int(float(string))
    imagename = "-image"+str(number+1)+".jpg"
    print(imagename)
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Documents/smartbin2/smartbin2-master/images/'+filename.imagename)
    camera.stop_preview()

def identify():
    url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
    files = (os.listdir("/home/pi/Documents/smartbin2/smartbin2-master/images"))
    lastfile = files[-1]
    data = {'file': open('/home/pi/Documents/smartbin2/smartbin2-master/images/'+lastfile, 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}
    #data = {'file': open('./images/image2.jpg', 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}
    response = requests.post(url, auth= requests.auth.HTTPBasicAuth('GvqHLwBkqU4tpSyXDU471CG6K1y5XYw8', ''), files=data)
    print(response.text)
    data = json.loads(response.text)
    a = data["result"][0]["prediction"][0]["label"]
    print(a)

#open and close plate specified in the argument
def openplate():
    GPIO.setup(18,GPIO.OUT)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(3)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    #add complete variable for the plate and return it

#rotate the top bin compartment
def rotate():
    GPIO.setup(6,GPIO.OUT)
    print "LED on"
    GPIO.output(6,GPIO.HIGH)
    time.sleep(3)
    print "LED off"
    GPIO.output(6,GPIO.LOW)

#proximity sensor to identify presence of an object in bin entry compartment
def itemsensor():
    sensor = DistanceSensor(echo=24, trigger=23)
    object = False
    count = 0
    #check 5 times in 5 seconds, set object variable accordingly
    for x in range(5):
        dist = sensor.distance * 100
        if dist < 10:
            count = count + 1
            if count = 5:
                object = True
        sleep(1)
    return(object)

#proximity sensor to identify when the door is open or closed
def door():
    sensor = DistanceSensor(echo=19, trigger=26)
    object = False
    count = 0
    #check 5 times in 5 seconds, set object variable accordingly
    for x in range(2):
        dist = sensor.distance * 100
        if dist > 10:
            count = count + 1
            if count = 2:
                open = True
        sleep(1)
    return(open)

#an object has been put in the bin, rotate, and identify the object
def binstatus1(items):
    object = itemsensor()
    open = door()
    while object == False and open == True:
        object = itemsensor()
        open = door()
    if object == True:
        time.sleep(2)
        rotate() #rotate objects in the top compartment 90 degrees and update items
        photo() #capture image of the object and assign it to variable
        identify() #identify object in the image captured
        time.sleep(7) #wait 7 seconds for object identification
        items[1] = identify.a #assign object type to compartments array
        print(items)
        return(items)
    if object == False and open == False:
        return(items)

#the door is closed, empty any compartments which contain items
def binstatus2(items):
    while items != [0,0,0,0]:
        open = door()
        #for each element of the items array
        for i in range(1, 4):
            #check if the object is equal to the bottom compartment category
            if items[i-1] == i:
                platenumber = i
                #if object matches compartment category, empty the compartment
                openplate()
                items[i] = 0
                rotate()
            elif:
                rotate()
            if open == True:
                break
    return(items)

#initialise items array
items = [0,0,0,0]
power = True
while power == True:
    open = door()
    #if an object has been input to the bin, rotate and identify it
    if open == True:
        items = binstatus1(items)

    #check if another object has been input or is about to be input to the bin
    open = door()
    object = itemsensor()
    #while the door is open wait for object to be input or door to close
    if open == False:
        binstatus2(items)
