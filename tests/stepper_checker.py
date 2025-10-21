# Run this file to check Stepper Motor functionality
# Should turn around multiple times with increasing speed.

from dpeaDPi.DPiComputer import DPiComputer
from dpeaDPi.DPiStepper import *
from time import sleep

dpiStepper = DPiStepper()


dpiStepper.setBoardNumber(0)
if dpiStepper.initialize() != True:
    print("Communication with the DPiStepper board failed.")

dpiStepper.enableMotors(False) # Disabling in case previous program forgot to

microstepping = 8
dpiStepper.setMicrostepping(microstepping)


# Initial Values
speed_steps_per_second = 200 * microstepping
accel_steps_per_second_per_second = speed_steps_per_second
dpiStepper.setSpeedInStepsPerSecond(0, speed_steps_per_second)
dpiStepper.setAccelerationInStepsPerSecondPerSecond(0, accel_steps_per_second_per_second)

stepperStatus = dpiStepper.getStepperStatus(0)
currentPosition = dpiStepper.getCurrentPositionInSteps(0)[1]
print(f"Pos = {currentPosition}")
dpiStepper.enableMotors(True)

stepper_num = 0
steps = 1600
wait_to_finish_moving_flg = True

#Tries to do the for loop, if there's any errors OR when it's done, then execute the finally block
try:
    for i in range(1, 6):
        curr_speed = speed_steps_per_second * i
        curr_accel = accel_steps_per_second_per_second * i
        print(f"Speed = {curr_speed}")
        print(f"Acceleration = {curr_accel}")

        dpiStepper.setSpeedInStepsPerSecond(0, curr_speed)
        dpiStepper.setAccelerationInStepsPerSecondPerSecond(0, curr_accel)
        dpiStepper.moveToRelativePositionInSteps(stepper_num, steps, wait_to_finish_moving_flg)
        currentPosition = dpiStepper.getCurrentPositionInSteps(0)[1]
        print(f"Pos = {currentPosition} \n")
finally:
    dpiStepper.enableMotors(False)
