import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("API_KEY")


def main():
    print(f"{api_key}")


if __name__ == "__main__":
    main()
