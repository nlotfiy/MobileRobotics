import libomni as robot  #Library tha handles all the serial commands to arduino AtMega
import time
import numpy as np


#encoder odometry setup
oldEncoder0 = 0
oldEncoder1 = 0
oldEncoder2 = 0
newEncoder0 = 0
newEncoder1 = 0
newEncoder2 = 0

#odometry position setup
global current_x
global current_y
global current_theta
current_x = 0
current_y = 0
current_theta = 0 

#you can use this function to implement your inverse kinematic equations to calculate a RPM value to give the robot. Essentially your xd (x dot a.k.a x velocity) will be the value you pass in to move the robot in the x direction in meters per second. The same applies to yd. thetad will be your orientation and is in radians, for example 3.14 would be half a rotation a second.
def inv_kin(xd,yd,thetad):
	r = 0.03 # radius of each wheel [m]
	l = 0.19 # distance from each wheel to the point of reference [m]
 
	xd_des = xd # velocity in the x-direction in the local frame [m/s]
	yd_des = yd # velocity in the y-direction in the local frame [m/s]
	thd_des = thetad # velocity in the x-direction in the local frame [rad/sa]
 
	vel_des = np.array([xd_des,yd_des,thd_des]).reshape(3,1)
 
	FK_M = (2*np.pi*r/60)*np.array([1/np.sqrt(3),0,-1/np.sqrt(3),-1/3,2/3,-1/3,-1/(3*l),-1/(3*l),-1/(3*l)]).reshape(3,3) # Forward kinematics matrix
 
	IK_M = np.linalg.inv(FK_M) # Inverse kinematics matrix
 
	motor_spd_vec = np.dot(IK_M,vel_des, out=None)
 
	wheel0RPM = motor_spd_vec[0] # motor 2 speed [rpm]
	wheel1RPM = motor_spd_vec[1] # motor 1 speed [rpm]
	wheel2RPM = motor_spd_vec[2] # motor 3 speed [rpm]

	robot.motor_rpm(wheel0RPM,wheel1RPM,wheel2RPM) 

	
########################################################################		Encoder Odometry	
def odometryCalc(xk,yk,thetak,l=0.19, N=2249, r=0.03):
	global oldEncoder0
	global oldEncoder1
	global oldEncoder2
	
	newEncoder0 = robot.encoder(0)
	newEncoder1 = robot.encoder(1)
	newEncoder2 = robot.encoder(2)
	
# Your odometry code goes here









	oldEncoder0 = newEncoder0
	oldEncoder1 = newEncoder1
	oldEncoder2 = newEncoder2

	return  newPos_mat
				
try:

	start = time.time()
	t = 0
	dt = 0.1
	
	x_dot = float(input("Enter desired x velocity (max .5 m/s): "))
	y_dot = float(input("Enter desired y velocity (max .5 m/s): "))
	theta_dot = float(input("Enter desired angular velocity (max π rad/s): "))
	t_final  = float(input("Enter time to run: "))
	
	#set your old encoder values
	oldEncoder0 = robot.encoder(0)
	oldEncoder1 = robot.encoder(1)
	oldEncoder2 = robot.encoder(2)

	
	while t < t_final:
		
		xc = current_x
		yc = current_y
		thetac = current_theta
		
		#run the robot with the desired velocities
		inv_kin(x_dot,y_dot,theta_dot)
		
		#YOU HAVE TO ENTER YOUR COMMAND TO CALL THE FUNCTION FOR ENCODER ODOMETRY HERE
		#update the pose of the robot using encoder odometry
		pose = odometryCalc(xc,yc,thetac)

		#update the new value for robot current pose for next iteration
		current_x = pose.item(0)
		current_y = pose.item(1)
		current_theta = pose.item(2)
		
		#print the robot pose on terminal
		print_x = '{:.3f}'.format(current_x)
		print_y = '{:.3f}'.format(current_y)
		print_theta = '{:.3f}'.format(current_theta)
		
		data_pose = str(print_x)+" , "+str(print_y)+" , "+str(print_theta)
		print(data_pose)
		
		time.sleep(dt)
		t = t + dt
		
	robot.stop()

## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	robot.stop()    
	#~ file.close() 
	print('\n\n		Stop!!! See you again!')				
				
