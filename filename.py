import os
files = (os.listdir("/home/pi/Documents/smartbin2/smartbin2-master/images"))
#files = (os.listdir("./images"))
lastfile = files[-1]
ending = lastfile[6:]
string = ending[:-4]
number = int(float(string))
imagename = "-image"+str(number+1)+".jpg"
print(imagename)
