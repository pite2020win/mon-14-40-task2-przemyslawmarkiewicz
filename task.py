import random 
import time

class Airplane:
    def __init__(self):
        self.tilt = random.gauss(0, 10)

if __name__ == "__main__":

    airplane = Airplane()
    while True:
        print(f"Before correction: {airplane.tilt}")
        rate_of_correction = 1
        airplane.tilt = random.gauss(0, 2 * rate_of_correction)
        print(f"After correction: {airplane.tilt}")
        if airplane.tilt > rate_of_correction:
            rate_of_correction = airplane.tilt
        time.sleep(1)

