from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

client = genai.Client()


def generate_response(prompt, model="gemini-flash-lite-latest"):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text

        except Exception as error:
            print(f"Gemini request failed. Attempt {attempt + 1}/3")

            if attempt < 2:
                time.sleep(2)
            else:
                raise error