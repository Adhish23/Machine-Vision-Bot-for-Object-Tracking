from imutils.video import VideoStream
from reference.pid import PID
import imutils
import cv2
import time
import RPi.GPIO as GPIO
import os
import pigpio

MIN_ANG = 30 #degrees
MAX_ANG = 150 #degrees
MIN_PW = 800 # microseconds
MAX_PW = 2200 # microseconds

ANG_RANGE = MAX_ANG-MIN_ANG
PW_RANGE = MAX_PW-MIN_PW
PWAR = float(PW_RANGE)/ANG_RANGE

colorLower =(10,100,100)
colorUpper = (50,255,255)

panServo =  27
tiltServo = 17

panAngle = 90
tiltAngle = 90

prev = 0
vs = 0
p = 0 ###for y movement
r = 0 ###for x movement
move = 0

def motor_init():
    global motorPwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT) #enable pin of motor
    motorPwm = GPIO.PWM(21, 1000)
    motorPwm.start(0)

def left():
    GPIO.output(26, False)
    GPIO.output(19, True)
    GPIO.output(13, False)
    GPIO.output(6, True)
##    sleep(tf)
    
def right():
    GPIO.output(26, True)
    GPIO.output(19, False)
    GPIO.output(13, True)
    GPIO.output(6, False)
##    sleep(tf)
    
def forward():
    GPIO.output(26, True)
    GPIO.output(19, False)
    GPIO.output(13, False)
    GPIO.output(6, True)
##    sleep(tf)
    
def reverse():
    GPIO.output(26, False)
    GPIO.output(19, True)
    GPIO.output(13, True)
    GPIO.output(6, False)
##    sleep(tf)

def stop():
    GPIO.output(26, False)
    GPIO.output(19, False)
    GPIO.output(13, False)
    GPIO.output(6, False)
##    sleep(tf)

def driveMotor(dc):
    global motorPwm
    assert dc >=0 and dc <= 100
    ###dutyCycle = angle / 18. + 3.
    motorPwm.ChangeDutyCycle(dc)
######    time.sleep(0.3)
    


def system_init():
    global vs
    global p
    global r
    global panAngle
    global tiltAngle
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    os.system('sudo pigpiod')
    print("PIGPIOD STARTED!!!")
    time.sleep(1)
    motor_init()
    GPIO.setup(panServo, GPIO.OUT)
    GPIO.setup(tiltServo, GPIO.OUT)    
    positionServo(panServo, panAngle)
    positionServo(tiltServo, tiltAngle)
    
    # create a PID and initialize it
    p = PID(0.15, 0.04, 0.02)   #p.value, i.value, d.value 0.2, 0.06, 0.021
##    p = PID(1, 0.0, 0.0)
    p.initialize()
    # create a PID and initialize it
    r = PID(0.0017, 0.0001, 0.0002)###(1.0, 0.0 , 0.0) ###
    r.initialize()
    print("Waiting for for camera to warmup...")
    vs = VideoStream(0).start()
    time.sleep(2.0)

#position servo
def positionServo(servo,angle):
############    
############    global prev
############    assert angle >=0 and angle <= 180
############    pwm = GPIO.PWM(servo, 50)
############    pwm.start(prev)
############    dutyCycle = angle / 18. + 3.
############    pwm.ChangeDutyCycle(dutyCycle)   
############    time.sleep(0.3)
######################    pwm.stop()
############    prev = dutyCycle
############    time.sleep(0.2)
    assert MIN_ANG <= angle <= MAX_ANG
    pi = pigpio.pi()
    angle = (MIN_PW + ((angle - MIN_ANG) * PWAR))
    pi.set_servo_pulsewidth(servo, angle)
##    time.sleep(0.1)
    pi.stop()

def mapServo(x,y):
    global move
######    if(x>=0 and x<= 180):
######        positionServo(panServo, x)
######    if(y>=0 and y<=180):
######        positionServo(tiltServo, y)
    y = y//2
    x = round( x/2, 2)
##    print("X->{0}".format(y))
    #time.sleep(0.08)
    if(y < 0):
        if(y< -60):
            y = 0
            p.initialize()
        
##########    for k in range(0,int(abs(y))):
        tilt = 90 + abs(y)
        positionServo(tiltServo, tilt)
        #time.sleep(0.1)
##        print("opX->{0} & opY->{1}".format(x, tilt))
    if(y > 0):
        if(y> 60):
            y = 0
            p.initialize()
        
##########    for k in range(0,int(abs(y))):
        tilt = 90 - abs(y)
        positionServo(tiltServo, tilt)
        #time.sleep(0.1)
##        print("opX->{0} & opY->{1}".format(x, tilt))
##    if(y == 0):
##        positionServo(tiltServo, 90)
##        #time.sleep(0.1)
##        print("opX->{0} & opY->{1}".format(x, y))

########################################
    if(x > 0):
        if(x > 0.2):
            x = 0
            r.initialize()
            
        driveMotor(50)
        left()
        time.sleep(x)#0.65  x
        stop()
        
    if(x < 0):
        if(x < -0.2):
            x = 0
            r.initialize()
        
        driveMotor(50)###abs(x)
        right()
        time.sleep(abs(x))#0.65  abs(x)
        stop()
        
    if(x >= -0.01 and x<= 0.01):
        stop()


def obj_center():
    global vs
    global motorPwm
    while True:
        
        # grab the next frame from the video stream, Invert 180o, resize the
        # frame, and convert it to the HSV color space
        frame = vs.read()
        frame = imutils.resize(frame, width=360, height=360)
        frame = imutils.rotate(frame, angle=180)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # calculate the center of the frame as this is where we will
        # try to keep the object
        (H,W) = frame.shape[:2]
        centerX = W//2
        centerY = H//2
        cv2.circle(frame, (centerX, centerY), 5, (0, 255, 0), -1)
        # construct a mask for the object color, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, colorLower, colorUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        # find contours in the mask and initialize the current
        # (x, y) center of the object
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        center = None
        # only proceed if at least one contour was found
        if len(cnts) > 0:
                #find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                (objX, objY) = center
                # only proceed if the radius meets a minimum size
                ###print("Radius:{0}".format(radius))
                if (radius > 50):
                    driveMotor(50)
                    reverse()
                    time.sleep(0.16)
                    stop()
                    
                elif (radius < 20):
                    driveMotor(50)
                    forward()
                    time.sleep(0.16)
                    stop()
                
                else:
                    stop()
                
####################                if radius > 10:
                    #Draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)

                    opY = pid_process(objY, centerY, 0)
                    opX = pid_process(objX, centerX, 1)
                    mapServo(opX, opY)
##                    print("[INFO] center->{0}\n".format(centerY))
##                    print("[INFO] object->{0}\n".format(objY))

        # show the frame to our screen
        cv2.imshow("Frame", frame)
        
##        p.initialize()
##        r.initialize()
##                    
        # if [ctrl+c] key is pressed, stop the loop
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c') or key == ord('C'):
            
            positionServo(panServo, 90)
            positionServo(tiltServo, 90)
            motorPwm.stop()
            stop()
            os.system('sudo killall pigpiod')
            GPIO.cleanup()
            cv2.destroyAllWindows()
            vs.stop()
            break

def pid_process(objCoord, centerCoord, motion):
    global p
    global r
    if(motion == 0):         
        # calculate the error
        error = centerCoord - objCoord
        # update the value
        output = p.update(error)
        
    if(motion == 1):
        # calculate the error
        error = centerCoord - objCoord
        # update the value
        output = r.update(error)
        
##########    print("o/p = {0}".format(output))
    return output


if __name__ == '__main__':
######    pi = piGPIO.pi()
    system_init()
    obj_center()
        
