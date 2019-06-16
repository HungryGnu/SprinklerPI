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
    return None

def run(zone, all=False):
    if all:
        for z in Zone.objects.all():
            openCloseValves(z.pin_number, z.run_duration)
    elif zone in Zone.objects.all().values('zone_number'):
        z = Zone.objects.get(zone_number=zone)
        openCloseValves(z.zone_number, z.run_duration)
    gpio.cleanup()
    return None

if __name__== '__main__':
    try:
        run(all=True)
    except:
        # Shut all valves!
        print("DISASTER!")
        for num in Zone.objects.all().values_list('pin_number', flat=True):
            gpio.setup(num, gpio.OUT)
            gpio.output(num, gpio.HIGH)
        gpio.cleanup()
        print('Disaster Averted')
        raise
