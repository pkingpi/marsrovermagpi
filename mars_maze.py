# Mars Rover Maze Navigator
# Press Ctrl-C to stop

import rover, time, random

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

hownear = 15.0
hownearside = 30.0
reversetime = 2
turntime = 2.5

# Rotate mast to front
rover.setServo(servo_MA, 0)

# Return True if the ultrasonic sensor detects an obstacle
def obstacle(localhownear, localhownearside):
    dist = rover.getDistance()
    print ("Distance: ", (int(dist * 10)) / 10.0)
    if dist < localhownear:
        rover.stop()
        print("Wall detected ahead")
        #turn mast to left
        rover.setServo(servo_MA,89)
        time.sleep(1)
        dist_left = rover.getDistance()
        print("Left distance: ", dist_left)
        #turn mast to right
        rover.setServo(servo_MA,-89)
        time.sleep(1)
        dist_right = rover.getDistance()
        print("Right distance: ", dist_right)
        rover.setServo(servo_MA, 0)
        time.sleep(0.5)

        if dist_left < localhownearside and dist_right >= localhownearside:
            # Wall on the left
            print("Wall detected on left")
            # Spin right
            spinR()
            time.sleep(turntime)
            rover.stop()

        elif dist_right < localhownearside and dist_left >= localhownearside:
            # Wall on the right
            print("Wall detected on right")
            # Spin left
            spinL()
            time.sleep(turntime)
            rover.stop()

        # Both side walls or no side walls
        else:
            if dist_right < localhownearside and dist_left < localhownearside:
                # Walls on left and right
                print("Walls detected on both sides")
                # Reverse a little
                goReverse()
                time.sleep(reversetime)
                rover.stop()         
            else:            
                print("No side walls detected")
            # Pick a random number to choose spin direction 
            coin = random.randint(0,1)
            if coin == 0:
                # Spin left
                print("Turning left")
                spinL()
                time.sleep(turntime)
                rover.stop()
            else:
                # Spin right
                print("Turning right")
                spinR()
                time.sleep(turntime)
                rover.stop()

try:
    # repeat the next indented block forever
    while True:
        goForward()
        time.sleep(0.1)
        obstacle(hownear, hownearside)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    pass

finally:
    rover.setServo(servo_MA, 0)
    rover.cleanup()
