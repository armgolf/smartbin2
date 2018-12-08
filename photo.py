from picamera import PiCamera
from time import sleep
import filename
camera = PiCamera()
camera.rotation = 180
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/smartbin2/smartbin2-master/images/'+filename.imagename)
camera.stop_preview()
