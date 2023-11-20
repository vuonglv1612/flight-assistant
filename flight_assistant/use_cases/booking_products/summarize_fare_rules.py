from flight_assistant.clients import FareRuleSummarizer


class SummarizeFareRulesUseCase:
    def __init__(
        self,
        summarizer: FareRuleSummarizer,
    ):
        self._summarizer = summarizer

    def execute(self, fare_rules: str) -> str:
        summary = self._summarizer.summarize(fare_rules)
        return summary
