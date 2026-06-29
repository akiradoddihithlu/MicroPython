
import machine
import os
import time

def multicolor():
    blue = machine.Pin(13, machine.Pin.OUT)
    green = machine.Pin(12, machine.Pin.OUT)
    red = machine.Pin(11, machine.Pin.OUT)
    sleeptime=1
    while True:
        for bluevalue in range(2):
            blue.value(bluevalue)
            time.sleep(sleeptime)
            for greenvalue in range (2):
                green.value(greenvalue)
                time.sleep(sleeptime)
                for redvalue in range (2):
                    print(redvalue)
                    red.value(redvalue)
                    time.sleep(sleeptime)