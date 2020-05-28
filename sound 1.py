import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(40, gpio.OUT)
while True:
    half_wl = 0.0001
    
    gpio.output(40, gpio.HIGH)
    time.sleep(half_wl)
    gpio.output(40, gpio.LOW)
    time.sleep(half_wl)
    
