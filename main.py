import os

from dotenv import load_dotenv

load_dotenv()


def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    print(f"Your OpenAI API Key is: {openai_api_key}")
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
