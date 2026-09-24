import argparse
import json
import os
from call_function import available_functions, call_function
from prompts import system_prompt


# PEP 8 style convention (stdlib imports, blank line, then third-party imports)
from dotenv import load_dotenv
from openai import OpenAI

def main() -> None:

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None: # if not api_key
        raise RuntimeError("Error: OPENROUTER_API_KEY environment variable not found")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages: list[dict] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": args.user_prompt},
    ]

    generate_content(client, messages, args)

def generate_content(client: OpenAI, messages: list, args) -> None:

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        # print(f"User prompt: {messages["content"]}") fails because TypeError: list indices must be integers or slices, not str, see list indexing vs. dictionary key lookup

        if response.usage is None:
            raise RuntimeError("Error: failed API request")

        prompt_tokens: int = response.usage.prompt_tokens
        completion_tokens: int = response.usage.completion_tokens

        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {completion_tokens}")

    # no dict/map indexing needed here. response isn't a dictionary — it's an object (an instance of a Pydantic model that the OpenAI SDK defines), so you access its fields with dot notation, the same way you're already doing with response.choices[0].message.content. how was i suppose to know that
    message = response.choices[0].message # grabbing the message

    if message.tool_calls: #type?
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
            result_message = call_function(tool_call, args.verbose)
            if not result_message["content"]:
                raise Exception("Error: The returned tool message should have a non-empty 'content'")
            elif args.verbose:
                print(f"-> {result_message['content']}")
            else:
                print(result_message)
    else:
        print(f"Response: {message.content}")

if __name__ == "__main__":
    main()