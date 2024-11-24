from Adafruit_PCA9685 import PCA9685
import time

pwm = PCA9685()
pwm.set_pwm_freq(60)

def move_forward():
    """
    Moves the robot forward by adjusting servo positions.
    """
    print("Moving forward...")
    pwm.set_pwm(0, 0, 400)
    time.sleep(0.5)
    pwm.set_pwm(0, 0, 300)
    print("Forward movement complete.")
