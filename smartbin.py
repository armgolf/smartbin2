import time #required for pausing the script

#open and close plate specified in the argument
def openplate(platenumber):
    tbd

#proximity sensor to identify presence of an object in bin entry compartment
def itemsensor():
    object = True
    return(object)

#proximity sensor to identify when the door is open or closed
def door():
    open = True
    return(open)

#an object has been put in the bin, rotate, and identify the object
def binstatus1(items):
    time.sleep(2)
    import rotate #rotate objects in the top compartment 90 degrees and update items
    import photo #capture image of the object and assign it to variable
    import identify #identify object in the image captured
    time.sleep(7) #wait 7 seconds for object identification
    items[1] = identify.response #assign object type to compartments array
    return(items)

#the door is closed, empty any compartments which contain items
def binstatus2(items):
    for i in range(1, 4):
        if items != [0,0,0,0]
            for i in range(1, 4):
                if items[i-1] == i:
                    platenumber = i
                    openplate(platenumber)
                    items[i] = 0
                    import rotate

#initialise items array
items = [0,0,0,0]

while power == True:
    itemsensor()
    #if an object has been input to the bin, rotate and identify it
    if itemsensor.object == True:
        binstatus1(items)

    #check if another object has been input or is about to be input to the bin
    door()
    itemsensor()
    #while the door is open wait for object to be input or door to close
    while door.open == True and itemsensor.object == False:
        itemsensor()
        if itemsensor.object == True:
            binstatus1(items)
        elif door.open == False:
            binstatus2(items)

    #if there are items in the bin, empty the bin
    if items != [0,0,0,0]:
        binstatus2(items)
