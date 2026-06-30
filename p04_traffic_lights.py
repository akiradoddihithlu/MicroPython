from machine import Pin, UART, ADC, PWM
import time



class trafficlights: 
    def __init__(self):
        self.red= Pin(4, Pin.OUT)
        self.yellow=Pin(5, Pin.OUT)
        self.green=Pin(6, Pin.OUT)
        self.buzzer = PWM(Pin(3))

    def alllights(self):
        self.red.value(1)
        for x in range(4):
            self.play_tone(698, 300)
            self.play_tone(0, 200)
            self.play_tone(658, 300)
            self.play_tone(0, 200)
        #time.sleep(2)
        self.red.value(0)

        self.yellow.value(1)
        time.sleep(2)
        self.yellow.value(0)

        self.green.value(1)
        time.sleep(2)
        self.green.value(0)


    def play_tone(self, frequency, duration_ms):
        # # Frequencies for standard musical notes (C5, D5, E5, F5, G5, A5, B5, C6)
        # melody = [523, 587, 659, 698, 784, 880, 988, 1047]
  
        """Plays a specific frequency for a given duration in milliseconds."""
        if frequency == 0:
            self.buzzer.duty_u16(0)  # Treat 0 Hz as a rest (silence)
        else:
            self.buzzer.freq(frequency)
            self.buzzer.duty_u16(32768) # 50% duty cycle (32768 out of 65535) gives the cleanest square wave tone
        time.sleep_ms(duration_ms)
        
