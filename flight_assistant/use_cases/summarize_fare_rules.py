from typing import Dict

from flight_assistant.clients import FareRuleSummarizer, BookingProductRepository


class SummarizeFareRulesUseCase:
    def __init__(
        self,
        summarizer: FareRuleSummarizer,
        booking_product_repo: BookingProductRepository,
    ):
        self._summarizer = summarizer
        self._booking_product_repo = booking_product_repo

    def execute(self, booking_product_id: str):
        booking_product = self._booking_product_repo.find_by_id(booking_product_id)
        if not booking_product:
            # TODO: log error
            return
        booking_data = booking_product.data
        penalty_part = self._get_penalty_part(booking_data)
        summary = self._summarizer.summarize(penalty_part)

        new_booking_data = self._add_fare_rule_summary(booking_data, summary)
        booking_product.data = new_booking_data
        self._booking_product_repo.save(booking_product)

    def _add_fare_rule_summary(self, booking_data: Dict[str, str], summary: str):
        return booking_data

    def _get_penalty_part(self, booking_data) -> str:
        return ""
