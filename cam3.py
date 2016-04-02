import time
import datetime
import picamera

today = datetime.datetime.now().strftime("Flowerbed---%m-%d-%Y_%H:%M:%S")
str(today)
myFile = '/home/pi/camera/%s.jpg' % today



with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(myFile)


