import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from flight_assistant.api.dependencies import create_summarizer
from flight_assistant.use_cases.booking_products import (
    SummarizeFareRulesUseCase,
)

router = APIRouter()
logger = logging.getLogger(__name__)


class SummarizeFareRulesBody(BaseModel):
    fare_rules: str


class SummarizeFareRulesResponse(BaseModel):
    fare_rules: str
    summary: str


@router.post("/fare-rules-summary", response_model=SummarizeFareRulesResponse)
def summarize_fare_rules(
    body: SummarizeFareRulesBody,
    summarizer=Depends(create_summarizer),
):
    use_case = SummarizeFareRulesUseCase(summarizer)
    summary = use_case.execute(body.fare_rules)
    return SummarizeFareRulesResponse(fare_rules=body.fare_rules, summary=summary)
