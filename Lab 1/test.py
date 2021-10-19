import libomni as robot  #Library tha handles all the serial commands to arduino AtMega
import time

try:
	while True:
		motorNum = input("Enter motor number (0-2): ")    
		motorPWM = float(input("Enter motor PWM value (0-255, Pos(+) is CCW, Neg(-) is CW: "))

		if motorNum == "0":
			robot.motor_pwm(motorPWM,0,0)
		elif motorNum == "1":
			robot.motor_pwm(0,motorPWM,0)
		elif motorNum == "2":
			robot.motor_pwm(0,0,motorPWM)		

	
## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	robot.stop()    
	#~ file.close() 
	print('\n\n		Stop!!! See you again!')
