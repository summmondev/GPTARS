import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt):
    """
    Generate text based on a given prompt using OpenAI GPT.
    :param prompt: The input prompt for the AI model.
    :return: AI-generated response as a string.
    """
    try:
        print("Generating text response...")
        response = openai.Completion.create(
            engine="text-davinci-003",  # Replace with the appropriate GPT model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        generated_text = response.choices[0].text.strip()
        print(f"Generated text: {generated_text}")
        return generated_text
    except Exception as e:
        print(f"Error generating text: {e}")
        return "Sorry, I encountered an error while generating a response."

# Example usage
if __name__ == "__main__":
    test_prompt = "Write a humorous tweet about robots taking over Twitter."
    result = generate_text(test_prompt)
    print(result)

