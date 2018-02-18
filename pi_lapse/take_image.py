from time import sleep
import picamera
import datetime
import os


def assure_path_exists(path):
    dir = os.path.dirname(path)
    print(dir)
    if not os.path.exists(dir):
        print('making dir!!')
        os.makedirs(dir)


base_dir = '/home/alex/timelapses/'

now = datetime.datetime.now()

# Create todays directory if it does not exist
todays_dir = '%s/%s/' % (base_dir, now.strftime("%Y%m%d"))
assure_path_exists(todays_dir)

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.framerate = 30
    sleep(2)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    camera.capture(todays_dir + now.strftime("%Y-%m-%d_%H%M%S") + '.jpg')

