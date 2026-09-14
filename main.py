# def main():
#     print("Hello from python-ai-agent!")


# if __name__ == "__main__":
#     main()

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RunTimeError("Error: environment variable not found")

from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)

print(response.choices[0].message.content)