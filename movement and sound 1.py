from sense_hat import SenseHat
import math
import RPi.GPIO as gpio
import time
sense = SenseHat()
sense.clear()
max_z = 0
gpio.setmode(gpio.BCM)
gpio.setup(40, gpio.OUT)
while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        accel_tot = math.sqrt(x*x+y*y+z*z)
        
        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)
        accel_tot = round(accel_tot, 0)
        
        if z > max_z:
            max_z = z
        
        print("x = {0}, y = {1}, z = {2}, max_z = {3}, accel_tot = {4}".format(x, y, z, max_z, accel_tot))

        half_wl = -0.0202427143*accel_tot + 0.17
        if half_wl<0:
            half_wl=0.17
    
        gpio.output(40, gpio.HIGH)
        time.sleep(half_wl)
        gpio.output(40, gpio.LOW)
        time.sleep(half_wl)
