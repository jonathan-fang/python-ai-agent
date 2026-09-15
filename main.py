import argparse
import os


# PEP 8 style convention (stdlib imports, blank line, then third-party imports)
from dotenv import load_dotenv
from openai import OpenAI

# standard convention use main()
def main() -> None:

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None: # if not api_key
        # RuntimeError not RunTimeError -- asked ai tutor
        raise RuntimeError("Error: OPENROUTER_API_KEY environment variable not found")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages: list[dict] = [
            {
                "role": "user",
                "content": args.user_prompt,
            }
    ]

    generate_content(client, messages)

def generate_content(client: OpenAI, messages: list) -> None:

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    print(f"User prompt: {messages[0]["content"]}") # or print(f'User prompt: {messages[0]["content"]}')
    # print(f"User prompt: {messages["content"]}") fails because TypeError: list indices must be integers or slices, not str, see list indexing vs. dictionary key lookup

    if response.usage is None:
        raise RuntimeError("Error: failed API request")

    prompt_tokens: int = response.usage.prompt_tokens
    completion_tokens: int = response.usage.completion_tokens

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {completion_tokens}")

    print(f"Response: {response.choices[0].message.content}")
    # print("Response: ")
    # print(response.choices[0].message.content)

    # no dict/map indexing needed here. response isn't a dictionary — it's an object (an instance of a Pydantic model that the OpenAI SDK defines), so you access its fields with dot notation, the same way you're already doing with response.choices[0].message.content. how was i suppose to know that

# use this thing to guard
if __name__ == "__main__":
    main()