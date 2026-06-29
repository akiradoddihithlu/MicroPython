
import machine
import gc
import os
import time

# Check available memory (Utilizing the 8MB PSRAM)
def onboard_memory():
    gc.collect()
    free_ram = gc.mem_free()
    total_ram = gc.mem_alloc() + free_ram

    print("--- Board Info ---")
    print(f"Total RAM available: {total_ram / 1024 / 1024:.2f} MB")

#blink
def blink_led():
    pin_num=14
    while True:
        try:
            led = machine.Pin(pin_num, machine.Pin.OUT)
            led.value(1) # Try to turn it on
            print(f"Testing Pin {pin_num}... blink onboard LED")
        except:
            print(f'Error  ')
        time.sleep(3)


        try:
            led = machine.Pin(pin_num, machine.Pin.OUT)
            led.value(0) # Try to turn it on
            print(f"Testing Pin {pin_num}... blink onboard LED")
        except:
            pass
        time.sleep(1)
