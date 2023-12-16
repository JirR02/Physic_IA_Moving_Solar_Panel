import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinLDR = 7


def rc_time(pinLDR):
    count = 0
    GPIO.setup(pinLDR, GPIO.OUT)
    GPIO.output(pinLDR, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pinLDR, GPIO.IN)
    while GPIO.input(pinLDR) == GPIO.LOW:
        count += 1
    return count


try:
    while True:
        with open("Lightvalues_Static.txt", "a") as f:
            f.write(str(rc_time(pinLDR)))
            print(rc_time(pinLDR))
            time.sleep(300)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
