from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import RPi.GPIO as GPIO
import time

kit = MotorKit()

pinLDR = 4

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
        for k in range(32):
            kit.stepper1.onestep()
        LightValueInitial = rc_time(pinLDR)
        kit.stepper1.onestep()
        LightValueNewForward = rc_time(pinLDR)
        time.sleep(0.5)
        for k in range(64):
            kit.stepper1.onestep(direction=stepper.BACKWARD)
        LightValueNewBackward = rc_time(pinLDR)
        time.sleep(0.5)
        for k in range(32):    
            kit.stepper1.onestep()
        if LightValueInitial > LightValueNewForward:
            while LightValueInitial > LightValueNewForward:
                LightValueInitial = LightValueNewForward
                time.sleep(0.5)
                for k in range(32):
                    kit.stepper1.onestep()
                LightValueNewForward = rc_time(pinLDR)
                time.sleep(0.5)
                if LightValueInitial < LightValueNewForward:
                    for k in range(32):
                        kit.stepper1.onestep(direction=stepper.BACKWARD)
        if LightValueInitial > LightValueNewBackward:    
            while LightValueInitial > LightValueNewBackward:
                LightValueInitial = LightValueNewBackward
                time.sleep(0.5)
                for k in range(32):
                    kit.stepper1.onestep(direction=stepper.BACKWARD)
                LightValueNewBackward = rc_time(pinLDR)
                time.sleep(0.5)
                if LightValueInitial < LightValueNewBackward:
                    for k in range(32):        
                        kit.stepper1.onestep()
        for k in range(32):
            kit.stepper2.onestep()
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
        time.sleep(0.5)
        for k in range(64):    
            kit.stepper2.onestep(direction=stepper.BACKWARD)
        LightValueNewBackward = rc_time(pinLDR)
        time.sleep(0.5)
        for k in range(32):
            kit.stepper2.onestep()
        if LightValueInitial > LightValueNewForward:
            while LightValueInitial > LightValueNewForward:
                LightValueInitial = LightValueNewForward
                time.sleep(0.5)
                for k in range(32):
                    kit.stepper2.onestep()
                LightValueNewForward = rc_time(pinLDR)
                time.sleep(0.5)
                if LightValueInitial > LightValueNewForward:
                    for k in range(32):
                        kit.stepper2.onestep(direction=stepper.BACKWARD)
        if LightValueInitial > LightValueNewBackward:    
            while LightValueInitial < LightValueNewBackward:
                LightValueInitial = LightValueNewBackward
                time.sleep(0.5)
                for k in range(32):    
                    kit.stepper2.onestep(direction=stepper.BACKWARD)
                LightValueNewBackward = rc_time(pinLDR)
                time.sleep(0.5)
                if LightValueInitial > LightValueNewBackward:
                    for k in range(32):
                        kit.stepper2.onestep()
        with open('Lightvalues_Moving.txt', 'a') as f:
            f.write(str(rc_time(pinLDR)))
        print(rc_time(pinLDR))
        time.sleep(300)
finally:
    GPIO.cleanup()
