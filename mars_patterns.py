# Mars Rover Movement Patterns
# Press Ctrl-C to stop

import rover, time

# Servo numbers
servo_FL = 9
servo_RL = 11
servo_FR = 15
servo_RR = 13
servo_MA = 0

def goForward():
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.forward(speed)

def goReverse():
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.reverse(speed)

def goLeft():
    rover.setServo(servo_FL, -20)
    rover.setServo(servo_FR, -20)
    rover.setServo(servo_RL, 20)
    rover.setServo(servo_RR, 20)

def goRight():
    rover.setServo(servo_FL, 20)
    rover.setServo(servo_FR, 20)
    rover.setServo(servo_RL, -20)
    rover.setServo(servo_RR, -20)

def spinL():
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.spinLeft(speed)

def spinR():
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.spinRight(speed)

speed = 60

rover.init(0)

def pattern():
    goForward()
    time.sleep(2)
    goReverse()
    time.sleep(2)
    goForward()
    goLeft()
    time.sleep(2)
    goRight()
    time.sleep(2)
    rover.stop()

def circle():
    goForward()
    goRight()
    time.sleep(40)
    rover.stop()

def square():
    for i in range(4):
        goForward()
        time.sleep(5)
        spinR()
        time.sleep(2.5)   
    rover.stop()

pattern()
time.sleep(2)
circle()
time.sleep(2)
square()

