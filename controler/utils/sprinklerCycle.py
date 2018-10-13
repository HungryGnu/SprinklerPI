#! /usr/bin/python3

import RPi.GPIO as gpio
from controler.models import Zone
import time


def openCloseValves(valve, time_):
    print('Starting sprinklers...')
    time.sleep(0.5)
    gpio.setup(valve, gpio.OUT)
    gpio.output(valve, gpio.LOW)
    time.sleep(time_)
    gpio.output(valve, gpio.HIGH)
    time.sleep(0.5)
    print('Zone Done!')
    return None

def run(all=False, zone):
    
    if all:
        openCloseValves(zones['zone1'][0], zones['zone1'][1])
        openCloseValves(zones['zone2'][0], zones['zone2'][1])
        openCloseValves(zones['zone3'][0], zones['zone3'][1])
        openCloseValves(zones['zone4'][0], zones['zone4'][1])

    gpio.cleanup()

if __name__=='__main__':
    try:
        run()
    except:
        # Shut all valves!
        print("DISASTER!")
        for num in zone:
            gpio.setup(num, gpio.OUT)
            gpio.output(num, GPIO.HIGH)
        gpio.cleanup()
        print('Disaster Averted')
        raise
