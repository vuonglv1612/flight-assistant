from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from openai import APIConnectionError, InternalServerError, OpenAI, RateLimitError

from flight_assistant.clients.utils import retry


class FareRuleSummarizer(ABC):
    @abstractmethod
    def summarize(self, fare_rules: str) -> str:
        pass


class OpenAISummarizer(FareRuleSummarizer):
    DEFAULT_SUMMARIZE_SETTINGS = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.2,
        "max_tokens": 512,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    DEFAULT_PROMPT = (
        "Please provide a summary of change fees and cancellation fees. Skip introduction and "
        "conclusion, start with the main point"
    )

    def __init__(
        self,
        openai_client: OpenAI,
        prompt: Optional[str] = None,
        summarize_config: Optional[Dict[str, Any]] = None,
    ):
        self._client = openai_client
        self._prompt = prompt or self.DEFAULT_PROMPT
        self._summarize_config = summarize_config or self.DEFAULT_SUMMARIZE_SETTINGS

    def summarize(self, fare_rules: str) -> str:
        @retry(
            max_attempt=3,
            delay=1,
            exceptions=(APIConnectionError, InternalServerError, RateLimitError),
        )
        def summarize_by_openai():
            response = self._client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Just give the summary"},
                    {"role": "user", "content": fare_rules},
                    {"role": "user", "content": self._prompt},
                ],
                **self._summarize_config
            )
            return response.choices[0].message.content

        return summarize_by_openai()
