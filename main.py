from p99_distance import US
import time

measure=US()

while True:
    dist = measure.get_distance()
    print(dist)
    time.sleep(1)
