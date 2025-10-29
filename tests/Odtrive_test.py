from dpea_odrive.odrive_helpers import *
from time import sleep

od = find_odrive("386037573437")
assert od.config.enable_brake_resistor is True, "Check for faulty brake resistor."

ax = ODriveAxis(od.axis1)
ax.set_gains()
if not ax.is_calibrated():
    print("calibrating...")
    ax.calibrate()
    
ax.set_vel_limit(10)
print("Speeding Up")
ax.set_ramped_vel(5, 1)
sleep(10)
print("Slowing Down")
ax.set_ramped_vel(0, 1)
ax.wait_for_motor_to_stop()
print("Current Position in Turns = ", round(ax.get_pos(), 2))
ax.idle()