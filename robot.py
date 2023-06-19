# Code language:Python
import RPi.GPIO as GPIO #Import library for working with GPIO
import time #Import a library for working with time
GPIO.setmode(GPIO.BOARD) #Setting the GPIO operation mode
enA = 38
enB = 40
in1 = 31
in2 = 33
in3 = 35
in4 = 37
GPIO.setup(in1, GPIO.OUT) #Setting pin 31 to output mode
GPIO.setup(in2, GPIO.OUT) #Setting pin 33 to output mode
GPIO.setup(in3, GPIO.OUT) #Setting pin 35 to output mode
GPIO.setup(in4, GPIO.OUT) #Setting pin 37 to output mode
GPIO.setup(enA, GPIO.OUT) #Setting pin 38 to output mode
GPIO.setup(enB, GPIO.OUT) #Setting pin 40 to output mode
pwmA = GPIO.PWM(enA, 1000) #Setting the PWM frequency on pin 40
pwmB = GPIO.PWM(enB, 1000) #Setting the PWM frequency on pin 38
pwmA.start(0)
pwmB.start(0)
trigPin = 11
echoPin = 13
Pin = 12
GPIO.setup(trigPin, GPIO. OUT) #Set pin 11 to режим output mode
GPIO.setup(echoPin, GPIO.IN) #Set pin 13 to input mode
GPIO.setup(Pin, GPIO.OUT) #Setting pin 12 to output mode
sRight = 12
sLeft = 2
sCentre = 7
pwm = GPIO.PWM(Pin, 50)
pwm.start(0)
def ultrasonic(): #Function for working with the distance sensor
    GPIO.output(trigPin, 0)
    time.sleep(2E-6)
    GPIO.output(trigPin, 1)
    time.sleep(10E-6)
    GPIO.output(trigPin,0)
    while GPIO.input(echoPin) == 0:
        global echoStart
        echoStart = time.time()
    while GPIO.input(echoPin) == 1:
        global echoStop
        echoStop = time.time()
    timet = echoStop - echoStart
    return int((34300*timet)/2)
    time.sleep(.2)
def servo(DutyCycle): #Function for working with the servo
    pwm.ChangeDutyCycle(DutyCycle)
def front(): #Function for moving forward
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    pwmA.ChangeDutyCycle(80)
    GPIO.output(in3,1)
    GPIO.output(in4,0)
    pwmB.ChangeDutyCycle(80)
def back(): #Function for moving backwards
    GPIO.output(in1,0)
    GPIO.output(in2,1)
    pwmA.ChangeDutyCycle(80)
    GPIO.output(in3,0)
    GPIO.output(in4,1)
    pwmB.ChangeDutyCycle(80)
def stop (): #Function to stop
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
def left (): #Function for turning left
    GPIO.output(in1,0)
    GPIO.output(in2,1)
    pwmA.ChangeDutyCycle(80)
    GPIO.output(in3,1)
    GPIO.output(in4,0)
    pwmB.ChangeDutyCycle(80)
def right(): #Function for turning right
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    pwmA.ChangeDutyCycle(80)
    GPIO.output(in3,0)
    GPIO.output(in4,1)
    pwmB.ChangeDutyCycle(80)
try: 
   while True: #Infinite loop
       servo(7.5) #Setting the angle of rotation of the servo
        time.sleep(.5)
        middledistance = ultrasonic() 
       if middledistance <= 30: #If the distance to the obstacle is less than or equal to 30 cm
            stop()
            time.sleep(.5)
            servo(sLeft)
            time.sleep(1)
            leftdistance = ultrasonic()
            print("left = ", leftdistance)
            time.sleep(.5)
            servo(sCentre)
            time.sleep(1)
            servo(sRight)
            time.sleep(1)
            rightdistance = ultrasonic()
            print("right = ", rightdistance)
            time.sleep(.5)
            servo(sCentre)
            time.sleep(1)
            if rightdistance <=30 and leftdistance <=30: 
                back()
                time.sleep(.5)
            elif leftdistance > rightdistance:
                left()
                time.sleep(.35)
            elif rightdistance > leftdistance:
                right()
                time.sleep(.35)
            else:
                front()
        else:
            front()
except KeyboardInterrupt: #Ctrl+C
    print("That's all!")
finally:
 GPIO. cleanup() #Clearing pins
