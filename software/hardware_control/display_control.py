from Adafruit_PCA9685 import PCA9685
import time

def initialize_display():
    """
    Initializes the robot's LCD or OLED display.
    """
    print("Initializing display...")
    time.sleep(1)
    print("Display ready!")

def display_message(message):
    """
    Displays a message on the robot's screen.
    :param message: The string to be displayed.
    """
    print(f"Displaying message: {message}")

# Example usage
if __name__ == "__main__":
    initialize_display()
    display_message("Hello! I am GPTARS!")
