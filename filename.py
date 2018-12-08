#import os
#files = (os.listdir("/home/pi/Documents/smartbin2/smartbin2-master/images"))
#files = (os.listdir("./images"))
#lastfile = files[-1]
#ending = lastfile[6:]
#string = ending[:-4]
#number = int(float(string))
#imagename = "-image"+str(number+1)+".jpg"
#print(imagename)

import os
path = './images'
name_list = os.listdir(path)
full_list = [os.path.join(path,i) for i in name_list]
time_sorted_list = sorted(full_list, key=os.path.getmtime)
sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
lastfile = sorted_filename_list[-1]
print(lastfile)
ending = lastfile[6:]
string = ending[:-4]
number = int(float(string))
imagename = "-image"+str(number+1)+".jpg"
print(imagename)
