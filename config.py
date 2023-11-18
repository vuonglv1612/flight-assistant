import environs

env = environs.Env()
env.read_env()

API_HOST = env.str("API_HOST", "localhost")
API_PORT = env.int("API_PORT", 8000)
ENGINE_POSTGRES_URI = env.str(
    "ENGINE_POSTGRES_URI", "postgresql://localhost/flight_assistant"
)

OPENAI_API_KEY = env.str("OPENAI_API_KEY", "OPENAI_API_KEY")

OPENAI_SUMMARIZE_PROMPT = (
    "Please provide a summary of change fees and cancellation fees. Skip introduction and "
    "conclusion, start with the main point"
)
OPENAI_SUMMARIZE_SETTINGS = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.2,
    "max_tokens": 512,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}
