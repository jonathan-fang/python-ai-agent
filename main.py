import os
import argparse

# PEP 8 style convention (stdlib imports, blank line, then third-party imports)
from dotenv import load_dotenv
from openai import OpenAI

# standard convention use main()
def main() -> None:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None: # if not api_key
        # RuntimeError not RunTimeError -- asked ai tutor
        raise RuntimeError("Error: OPENROUTER_API_KEY environment variable not found")
    
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

    messages: list[dict] = [
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            }
    ]
    user_prompt = messages[0]["content"]
    print(f"User prompt: {user_prompt}")

    # print(type(client.chat.completions.create))

    # if client.chat.completions.create[usage] is None:
    #     raise RuntimeError("Error: failed API request")

    # prompt_tokens = chat.completions.create[usage][prompt_tokens]
    # completion_tokens = chat.completions.create[usage][completion_tokens]

    if response.usage is None:
        raise RuntimeError("Error: failed API request")

    prompt_tokens: int = response.usage.prompt_tokens
    completion_tokens: int = response.usage.completion_tokens

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {completion_tokens}")

    # print(f"Response: {response.choices[0].message.content}") why doesnt this work?
    print("Response: ")
    print(response.choices[0].message.content)

    # no dict/map indexing needed here. response isn't a dictionary — it's an object (an instance of a Pydantic model that the OpenAI SDK defines), so you access its fields with dot notation, the same way you're already doing with response.choices[0].message.content. how was i suppose to know that

# use this thing to guard
if __name__ == "__main__":
    main()