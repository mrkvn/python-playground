import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    client = OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "You are very concise. \
                    You only do what you are told to do and you answer as short as possible.",
            },
            {"role": "user", "content": "Just reply TEST"},
        ],
    )

    print(completion.choices[0].message)


if __name__ == "__main__":
    main()
