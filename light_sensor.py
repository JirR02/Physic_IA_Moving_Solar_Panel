import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinLDR1 = 7
# pinLDR2 = Add pin Number

def rc_time1 (pinLDR1):
    count1 = 0
    GPIO.setup(pinLDR1, GPIO.OUT)
    GPIO.output(pinLDR1, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pinLDR1, GPIO.IN)
    while (GPIO.input(pinLDR1) == GPIO.LOW):
        count1 += 1
    return count1

# def rc_time2 (pinLDR2):
    # count2 = 0
    # GPIO.setup(pinLDR2, GPIO.OUT)
    # GPIO.output(pinLDR2, GPIO.LOW)
    # time.sleep(0.1)
    # GPIO.setup(pinLDR2, GPIO.IN)
    # while (GPIO.input(pinLDR1) == GPIO.LOW):
    #     count1 =+ 1
    # return count1

try:
    while True:
        print(rc_time1(pinLDR1))
        # print(rc_time1(pinLDR1))
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()