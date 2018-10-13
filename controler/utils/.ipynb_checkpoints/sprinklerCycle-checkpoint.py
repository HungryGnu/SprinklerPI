#! /usr/bin/python3

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

evenDay = True
runZone1 = True
runZone2 = True 
runZone3 = True

# Defines the pin controling each zone:
pins = [14, 15, 18, 23]



# Zone named to match the name structure of the current control box
# a dictionary of tuples, tuple contains (pin index, time in seconds)

zones = {
    "zone4" : (pins[0], 3),
    "zone3" : (pins[1], 5),
    "zone2" : (pins[2], 1),
    "zone1" : (pins[3], 3),
}

def setRunTime(zonesKey, minutes):
    # Takes as argument the zones dict above (or similar) time in minutes
    # Convert minutes to seconds
    time = minutes * 60
    # Set the zone.
    zones[zonesKey][0] = time
    return zones[zonesKey]

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

def run():
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
