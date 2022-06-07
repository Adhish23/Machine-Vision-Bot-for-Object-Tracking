from time import sleep
import RPi.GPIO as gpio
#GPIO.setmode(GPIO.BCM)
gpio.setwarnings(False)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(26, gpio.OUT)
    gpio.setup(19, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(21, gpio.OUT)##enable pin

def turn_left(tf):
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(13, False)
    gpio.output(6, True)
    sleep(tf)
    
def turn_right(tf):
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(13, True)
    gpio.output(6, False)
    sleep(tf)
    
def forward(tf):
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(13, False)
    gpio.output(6, True)
    sleep(tf)
    
def reverse(tf):
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(13, True)
    gpio.output(6, False)
    sleep(tf)

def stop(tf):
    gpio.output(26, False)
    gpio.output(19, False)
    gpio.output(13, False)
    gpio.output(6, False)
    sleep(tf)
    gpio.cleanup()
    
######    
######def driveMotor(enable,dc):
######    assert dc >=0 and dc <= 100
######    motorPwm = gpio.PWM(enable, 1000)
######    motorPwm.start(1)
######    ###dutyCycle = angle / 18. + 3.
######    motorPwm.ChangeDutyCycle(dc)
######    sleep(1)
######    motorPwm.stop()

    
def drive(direction, tym, dc):
    init()
    assert dc >=0 and dc <= 100
    motorPwm = gpio.PWM(21, 1000)
    motorPwm.start(1)
    ###dutyCycle = angle / 18. + 3.
    motorPwm.ChangeDutyCycle(dc)
######    sleep(1)
######    motorPwm.stop()

    if direction == "forward":
######        driveMotor(21, dc)
        forward(tym + 0.38)
        motorPwm.stop()
        stop(tym)
        
    elif direction == "reverse":
######        driveMotor(21, dc)
        reverse(tym +0.38)
        motorPwm.stop()
        stop(tym)

    elif direction == "left":
        turn_left(tym)
######        driveMotor(21, dc)
        motorPwm.stop()
        stop(tym)

    elif direction == "right":
        turn_right(tym)
######        driveMotor(21, dc)
        motorPwm.stop()
        stop(tym)

    elif direction == "stop":
        stop(tym)

    else :
        stop(tym)



if __name__ == '__main__':
	import sys
	drive((sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
	gpio.cleanup()

##
##init()
##forward(0.6)
##sleep(1)
##reverse(0.6)
##sleep(1)
##turn_right(0.6)
##sleep(1)
##turn_left(0.6)
##stop(1)
