import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def move_forward():
    pwm.set_pwm(0, 0, 300)
    time.sleep(0.5)
    pwm.set_pwm(0, 0, 400)

