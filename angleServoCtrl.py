#!/usr/bin/env python
#
#  Angle Servo Control 
#  Execute with parameter ==> sudo python3 servoCtrl.py <servo GPIO> <servo_angle> 
#
#  MJRoBot.org 01Feb18
################### CODE DOWNLOADED FROM WEB##################

######from time import sleep
######import RPi.GPIO as GPIO
######GPIO.setmode(GPIO.BCM)
######GPIO.setwarnings(False)
######import pigpio
######
########prev = 0
######
######def setServoAngle(servo, angle):
######	assert angle >=0 and angle <= 180
########	global prev
######	pwm = GPIO.PWM(servo, 50)
######	pwm.start(8)
######	dutyCycle = angle / 18. + 3.
######	pwm.ChangeDutyCycle(dutyCycle)
######	sleep(0.3)
######	pwm.stop()
########	prev = dutyCycle
######
######if __name__ == '__main__':
######	import sys
######	servo = int(sys.argv[1])
######	GPIO.setup(servo, GPIO.OUT)
######	setServoAngle(servo, int(sys.argv[2]))
######	GPIO.cleanup()

#####################CODE WITH PIGPIO##############################

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import pigpio
import math
import os
import sys
##prev = 0
MIN_ANG = 30 #degrees
MAX_ANG = 150 #degrees
MIN_PW = 800 # microseconds
MAX_PW = 2200 # microseconds

ANG_RANGE = MAX_ANG-MIN_ANG ### 150 - 30 = 120
PW_RANGE = MAX_PW-MIN_PW ### 2200 - 800 = 1400
PWAR = float(PW_RANGE)/ANG_RANGE ###1400/120 = 

def setServoAngle(servo, angle):
    
    os.system('sudo pigpiod')
    sleep(1)
    assert MIN_ANG <= angle <= MAX_ANG
    pi = pigpio.pi()
    angle = (MIN_PW + ((angle - MIN_ANG) * PWAR))
    pi.set_servo_pulsewidth(servo, angle)
    ##    time.sleep(0.1)
    pi.stop()
    os.system('sudo killall pigpiod')
    
if __name__ == '__main__':
	
	setServoAngle(int(sys.argv[1]), int(sys.argv[2]))
	GPIO.cleanup()


###################CODE WITH BOTH CODES IN A SINGLE LOOP################
######
######from time import sleep
######import RPi.GPIO as GPIO
######GPIO.setmode(GPIO.BCM)
######GPIO.setwarnings(False)
######import pigpio
######MIN_ANG = 30 #degrees
######MAX_ANG = 150 #degrees
######MIN_PW = 800 # microseconds
######MAX_PW = 2200 # microseconds
######
######ANG_RANGE = MAX_ANG-MIN_ANG
######PW_RANGE = MAX_PW-MIN_PW
######PWAR = float(PW_RANGE)/ANG_RANGE
######
######prev = 0
######
######def setServoAngle1(servo, angle):
######	assert MIN_ANG <= angle <= MAX_ANG
########	global prev
######	return MIN_PW + ((angle - MIN_ANG) * PWAR)
######
######def setServoAngle(servo, angle):
######	assert angle >=0 and angle <= 180
######	global prev
######	pwm = GPIO.PWM(servo, 50)
######	pwm.start(prev)
######	dutyCycle = angle / 18. + 3.
######	pwm.ChangeDutyCycle(dutyCycle)
######	sleep(0.1)
######	pwm.stop()
######	prev = dutyCycle
######	
######pi = pigpio.pi()
######if __name__ == '__main__':
######    import sys
######    servo = 17
######    GPIO.setup(servo, GPIO.OUT)
######    for x in range(30, 150, 15):
######            setServoAngle(servo, x)
######            sleep(1)
######    GPIO.cleanup()
######    sleep(5)
######    for y in range(30, 150, 15):
######            pw = setServoAngle1(servo, y)
######            pi.set_servo_pulsewidth(servo, pw)
######            sleep(1)
######    pi.set_servo_pulsewidth(servo,0)
