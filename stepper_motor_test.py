from adafruit_motorkit import MotorKit as kit
from adafruit_motor import stepper
import time

while True:
    kit.stepper1.onestep()
    kit.stepper1.onestep()
    kit.stepper1.onestep()
    kit.stepper1.onestep()
    kit.stepper1.onestep()
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep()
    kit.stepper2.onestep()
    kit.stepper2.onestep()
    kit.stepper2.onestep()
    kit.stepper2.onestep()
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD)
