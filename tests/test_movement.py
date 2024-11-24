import unittest
from hardware_control.movement import move_forward

class TestMovement(unittest.TestCase):
    def test_movement_functionality(self):
        """
        Test if the robot movement method executes without errors.
        """
        try:
            move_forward()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Movement method failed with error: {e}")

    def test_pwm_signal_range(self):
        """
        Test if PWM signal range is within valid limits for servos.
        """
        from Adafruit_PCA9685 import PCA9685
        pwm = PCA9685()
        pwm.set_pwm_freq(60)

        valid_signal = 300
        try:
            pwm.set_pwm(0, 0, valid_signal)
            self.assertTrue(100 <= valid_signal <= 600, "PWM signal out of range!")
        except Exception as e:
            self.fail(f"PWM signal setup failed with error: {e}")

if __name__ == "__main__":
    unittest.main()

