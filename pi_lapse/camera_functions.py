from picamera import PiCamera
from time import sleep
from fractions import Fraction


def save_long_exposure(filename, resolution=(1280, 720), exposure_time=6, iso=800):
    with PiCamera(resolution=resolution, framerate=Fraction(1,exposure_time), sensor_mode=3) as camera:
        camera.shutter_speed = exposure_time*10**6
        camera.iso = iso
        sleep(30)
        camera.exposure_mode = 'off'
        camera.capture(filename)
