import libomni as robot  #Library tha handles all the serial commands to arduino AtMega
import time
import numpy as np


#writing motor RPM
robot.motor_rpm(0,0,0) 
#reading motor RPM
print(robot.rpm(0))

#you can use this function to implement your inverse kinematic equations to calculate a RPM value to give the robot. Essentially your xd (x dot a.k.a x velocity) will be the value you pass in to move the robot in the x direction in meters per second. The same applies to yd. thetad will be your orientation and is in radians, for example 3.14 would be half a rotation a second.
def inv_kin(xd,yd,thetad):
	r = 0.03 # radius of each wheel [m]
	l = 0.19 # distance from each wheel to the point of reference [m]
 
	print(wheel0RPM)
	print(wheel1RPM)
	print(wheel2RPM)

	robot.motor_rpm(wheel0RPM,wheel1RPM,wheel2RPM) 

try:

	start = time.time()
	t = 0
	dt = 0.1
	
	x_dot = float(input("Enter desired x velocity (max .5 m/s): "))
	y_dot = float(input("Enter desired y velocity (max .5 m/s): "))
	theta_dot = float(input("Enter desired angular velocity (max π rad/s): "))
	t_final  = float(input("Enter time to run: "))

	while t < t_final:
		
		inv_kin(x_dot,y_dot,theta_dot)
		time.sleep(dt)
		t = t + dt
		
	robot.stop()

## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	robot.stop()    
	#~ file.close() 
	print('\n\n		Stop!!! See you again!')
