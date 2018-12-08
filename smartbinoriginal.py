import time #required for pausing the script

#open and close plate specified in the argument
def openplate():
    import openplate
    #add complete variable for the plate and return it

#rotate the top bin compartment
def rotate():
    import rotate

#proximity sensor to identify presence of an object in bin entry compartment
def itemsensor():
    import itemsensor
    object = itemsensor.object
    return(object)

#proximity sensor to identify when the door is open or closed
def door():
    import door
    open = door.open
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
        import rotate #rotate objects in the top compartment 90 degrees and update items
        import photo #capture image of the object and assign it to variable
        import identify #identify object in the image captured
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
