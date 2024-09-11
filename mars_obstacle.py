# Mars Rover Obstacle Detection 1
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

hownear = 15.0
reversetime = 2
turntime = 2.5

# Return True if the ultrasonic sensor detects an obstacle
def obstacle(localhownear):
    dist = rover.getDistance()
    print ("Distance: ", (int(dist * 10)) / 10.0)
    if dist < localhownear:
        return True
    else:
        return False

# Move back a little, then turn right
def avoid():
    # Back off a little
    goReverse()
    time.sleep(reversetime)
    rover.stop()

    # Spin right
    spinR()
    time.sleep(turntime)
    rover.stop()

try:
    # repeat the next indented block forever
    while True:
        goForward()
        time.sleep(0.1)
        if obstacle(hownear):
            rover.stop()
            avoid()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    pass

finally:
    rover.cleanup()
