from abc import ABC, abstractmethod


class FareRuleSummarizer(ABC):
    @abstractmethod
    def summarize(self, fare_rules: str) -> str:
        pass


class OpenAISummarizer(FareRuleSummarizer):
    def summarize(self, fare_rules: str) -> str:
        pass
