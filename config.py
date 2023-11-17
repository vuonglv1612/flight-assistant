import os


debug = int(os.getenv("DEBUG", 0))
if debug:
    import dotenv

    dotenv.load_dotenv()

OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

