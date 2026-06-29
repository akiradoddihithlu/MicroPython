from machine import Pin, UART, ADC
import time

class nightlight:
    def __init__(self): 
         pin_num=14
         self.led = Pin(pin_num, Pin.OUT)

        # self.sensor =Pin(16, Pin.IN)
         self.sensor = ADC(Pin(16))


    # def lamp(self):
    #     while True:
    #         if self.sensor.value()==True:
    #             self.led.value(1)
    #             print('its night timeee')
    #         else:
    #             self.led.value(0)
    #             print('its dayyyyy', self.sensor.value())

    def lamp2(self):
        # Set your custom threshold. 
        # Lower numbers = darker. You can tweak this value!
        dark_threshold = 20000 
        
        print("Nightlight sequence active. Monitoring raw photoresistor...")
        while True:
            # Read the raw analog value (returns a number between 0 and 65535)
            light_level = self.sensor.read_u16()
            
            # Print the raw value to your terminal so you can see it change
            print("Current Light Level:", light_level)
            
            # If the light drops below your threshold, turn on the LED
            if light_level < dark_threshold:
                self.led.value(1)
                print('Its night timeee!')
            else:
                self.led.value(0)
                print('Its dayyyyy.')
            
            time.sleep(0.5)
