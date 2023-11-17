from flight_assistant.use_cases import SummarizeFareRulesUseCase

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SummarizeFareRulesRequest(BaseModel):
    booking_product_id: str


class SummarizeFareRulesResponse(BaseModel):
    booking_product_id: str
    fare_rules: str
    fare_rules_summary: str


@router.post("/fare-rules-summary")
def summarize_fare_rules():
    pass
