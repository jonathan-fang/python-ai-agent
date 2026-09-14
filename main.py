import os
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

    print(response.choices[0].message.content)

# use this thing to guard
if __name__ == "__main__":
    main()