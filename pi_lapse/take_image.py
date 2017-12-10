from time import sleep
from picamera import PiCamera
import datetime


camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture("/home/alex/tl/" + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + '.jpg')