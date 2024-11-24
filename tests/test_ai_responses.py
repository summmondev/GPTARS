import unittest
from personality.responses import generate_response

class TestAIResponses(unittest.TestCase):
    def test_generate_response(self):
        """
        Test if the AI response generator works correctly.
        """
        mock_tweet = type("Tweet", (object,), {"user": type("User", (object,), {"screen_name": "test_user"})})()
        response = generate_response(mock_tweet)
        self.assertIn("GPTARS", response, "Generated response does not include GPTARS branding.")

    def test_response_length(self):
        """
        Test if the generated response is within a reasonable length.
        """
        mock_tweet = type("Tweet", (object,), {"user": type("User", (object,), {"screen_name": "test_user"})})()
        response = generate_response(mock_tweet)
        self.assertLessEqual(len(response), 280, "Response exceeds Twitter's character limit!")

if __name__ == "__main__":
    unittest.main()

