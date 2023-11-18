from flight_assistant.clients import BookingProductRepository, FareRuleSummarizer


class SummarizeFareRulesUseCase:
    def __init__(
        self,
        booking_product_repo: BookingProductRepository,
        summarizer: FareRuleSummarizer,
    ):
        self._booking_products = booking_product_repo
        self._summarizer = summarizer

    def execute(self, booking_product_id: str):
        booking_product = self._booking_products.find_by_id(booking_product_id)
        if not booking_product:
            return
        fare_rules = self._get_fare_rules(booking_product)
        for rule in fare_rules:
            penalty_part = self._get_penalty_part(rule)
            summary = self._summarizer.summarize(penalty_part)
            rule["summary"] = summary

        booking_product.update_fare_rules(fare_rules)
        self._booking_products.save(booking_product)
        return booking_product

    @staticmethod
    def _get_fare_rules(booking_product):
        return booking_product.data.get("fare", {}).get("fare_rules", [])

    @staticmethod
    def _get_penalty_part(fare_rule) -> str:
        rule_details = fare_rule.get("rule_details", [])
        penalty_parts = []
        for rule_detail in rule_details:
            category = rule_detail.get("category", "")
            if "penalties" in category.lower():
                penalty_parts.append(rule_detail.get("rules", ""))
        return "\n".join(penalty_parts)
