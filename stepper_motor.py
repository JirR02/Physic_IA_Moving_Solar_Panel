from adafruit_motorkit import MotorKit as kit
from adafruit_motor import stepper
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinLDR = 7

def rc_time (pinLDR):
    count = 0
    GPIO.setup(pinLDR, GPIO.OUT)
    GPIO.output(pinLDR, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pinLDR, GPIO.IN)
    while (GPIO.input(pinLDR) == GPIO.LOW):
        count += 1
    return count

LightValueInitial = rc_time(pinLDR)

try:
    while True:
        kit.stepper1.onestep()
        LightValueNewForward = rc_time(pinLDR)
        kit.stepper1.onestep(direction=stepper.BACKWARD)
        kit.stepper1.onestep(direction=stepper.BACKWARD)
        LightValueNewBackward = rc_time(pinLDR)
        kit.stepper1.onestep()
            if LightValueInitial > LightValueNewForward:
                while LightValueInitial > LightValueNewForward:
                    LightValueInitial = LightValueNewForward
                    kit.stepper1.onestep()
                    LightValueNewForward = rc_time(pinLDR)
                    if LightValueInitial < LightValueNewForward:
                        kit.stepper1.onestep(direction=stepper.BACKWARD)
            if LightValueInitial > LightValueNewBackward:    
                while LightValueInitial > LightValueNewBackward:
                    LightValueInitial = LightValueNewBackward
                    kit.stepper1.onestep(direction=stepper.BACKWARD)
                    LightValueNewBackward = rc_time(pinLDR)
                    if LightValueInitial < LightValueNewBackward:
                        kit.stepper1.onestep()
        kit.stepper2.onestep()
        LightValueNewForward = rc_time(pinLDR)
        kit.stepper2.onestep(direction=stepper.BACKWARD)
        kit.stepper2.onestep(direction=stepper.BACKWARD)
        LightValueNewBackward = rc_time(pinLDR)
        kit.stepper2.onestep()
        if LightValueInitial > LightValueNewForward:
            while LightValueInitial > LightValueNewForward:
                LightValueInitial = LightValueNewForward
                kit.stepper2.onestep()
                LightValueNewForward = rc_time(pinLDR)
                if LightValueInitial > LightValueNewForward:
                    kit.stepper2.onestep(direction=stepper.BACKWARD)
        if LightValueInitial > LightValueNewBackward:    
            while LightValueInitial < LightValueNewBackward:
                LightValueInitial = LightValueNewBackward
                kit.stepper2.onestep(direction=stepper.BACKWARD)
                LightValueNewBackward = rc_time(pinLDR)
                if LightValueInitial > LightValueNewBackward:
                    kit.stepper2.onestep()
        with open('Lightvalues_Moving.txt', 'a') as f:
            f.write(rc_time(pinLDR))
        time.sleep(300)
finally:
    GPIO.cleanup()
