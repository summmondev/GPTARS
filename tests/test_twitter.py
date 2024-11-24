import unittest
from twitter_integration.twitter_bot import start_twitter_bot

class TestTwitterBot(unittest.TestCase):
    def test_twitter_bot_initialization(self):
        """
        Test if the Twitter bot initializes without errors.
        """
        try:
            start_twitter_bot()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Twitter bot initialization failed with error: {e}")

    def test_tracked_accounts_presence(self):
        """
        Test if the tracked_accounts module contains the expected accounts.
        """
        from twitter_integration.tracked_accounts import tracked_accounts
        self.assertGreater(len(tracked_accounts), 0, "No accounts

