from twitter_integration.twitter_bot import start_twitter_bot
from hardware_control.movement import perform_movement_tests

if __name__ == "__main__":
    print("Starting GPTARS...")
    start_twitter_bot()
    perform_movement_tests()

