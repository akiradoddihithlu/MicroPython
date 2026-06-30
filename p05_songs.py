from machine import Pin, PWM
import time

class songs:
    def __init__(self):
        self.buzzer = PWM(Pin(3))
        self.notes_map = { 'C4': 261, 'D4': 294, 'E4': 330, 'F4': 349, 'G4': 392, 'A4':440, 'B4': 494
                          ,'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G5': 784, 'A5':880, 'B5': 988
                          ,'C6': 1047}

    def playsongs(self):
        rythm=['C5', 'C5', 'G5', 'G5', 'A5', 'A5', 'G5', 'G5', 'F5', 'F5', 'E5', 'E5', 'D5', 'D5', 'C5' ]
        for notes in rythm:
            if notes in self.notes_map:
                frequency=self.notes_map[notes]
            else:
                frequency=100

            self.play_tone(frequency,300, 100)


                    

    def play_tone(self, frequency, duration_ms, gap_ms):
        # # Frequencies for standard musical notes (C5, D5, E5, F5, G5, A5, B5, C6)
        # melody = [523, 587, 659, 698, 784, 880, 988, 1047]
        """Plays a specific frequency for a given duration in milliseconds."""
        if frequency == 0:
            self.buzzer.duty_u16(0)  # Treat 0 Hz as a rest (silence)
        else:
            self.buzzer.freq(frequency)
            self.buzzer.duty_u16(32768) # 50% duty cycle (32768 out of 65535) gives the cleanest square wave tone
        time.sleep_ms(duration_ms)

        self.buzzer.duty_u16(0)
        time.sleep_ms(int( gap_ms))
