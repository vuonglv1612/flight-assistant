from openai import OpenAI

import config
from flight_assistant.clients import OpenAISummarizer
from flight_assistant.engine.connection import create_session_factory

session_factory = create_session_factory(config.ENGINE_POSTGRES_URI)
openai_client = OpenAI(api_key=config.OPENAI_API_KEY)


def engine_session_factory():
    return session_factory()


def create_summarizer():
    return OpenAISummarizer(
        openai_client,
        summarize_config=config.OPENAI_SUMMARIZE_SETTINGS,
        prompt=config.OPENAI_SUMMARIZE_PROMPT,
    )
