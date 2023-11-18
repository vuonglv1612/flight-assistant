import logging
from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from flight_assistant.api.dependencies import create_summarizer, engine_session_factory
from flight_assistant.engine import SQLAlchemyBookingProductRepository
from flight_assistant.use_cases.booking_products import (
    GetBookingProductUseCase,
    ListBookingProductUseCase,
    SummarizeFareRulesUseCase,
)

router = APIRouter()
logger = logging.getLogger(__name__)


class BookingProductResponse(BaseModel):
    id: str
    data: Dict[str, Any]


class ListBookingProductsResponse(BaseModel):
    items: List[BookingProductResponse]
    page: int
    page_size: int
    total: int


@router.get("", response_model=ListBookingProductsResponse)
def list_booking_products(
        session=Depends(engine_session_factory), page: int = 1, page_size: int = 20
):
    booking_product_repo = SQLAlchemyBookingProductRepository(pg_session=session)
    use_case = ListBookingProductUseCase(booking_product_repo)
    result = use_case.execute(page, page_size)
    items = [
        BookingProductResponse(id=booking_product.id, data=booking_product.data)
        for booking_product in result["items"]
    ]
    return ListBookingProductsResponse(
        items=items,
        page=result["page"],
        page_size=result["page_size"],
        total=result["total"],
    )


class GetBookingProductResponse(BaseModel):
    id: str
    data: Dict[str, Any]


@router.get("/{id}", response_model=GetBookingProductResponse)
def get_booking_product(id: str, session=Depends(engine_session_factory)):
    booking_product_repo = SQLAlchemyBookingProductRepository(pg_session=session)
    use_case = GetBookingProductUseCase(booking_product_repo)
    booking_product = booking_product_repo.find_by_id(id)
    if not booking_product:
        logger.info("Booking product %s not found", id)
        raise HTTPException(
            status_code=404, detail={"error": "Booking product not found"}
        )
    return GetBookingProductResponse(id=booking_product.id, data=booking_product.data)


class SummarizeFareRulesResponse(BaseModel):
    id: str
    data: Dict[str, Any]


@router.post("/{id}/fare-rules-summary", response_model=SummarizeFareRulesResponse)
def summarize_fare_rules(
        id: str,
        session=Depends(engine_session_factory),
        summarizer=Depends(create_summarizer),
):
    booking_product_repo = SQLAlchemyBookingProductRepository(pg_session=session)
    use_case = SummarizeFareRulesUseCase(booking_product_repo, summarizer)
    booking_product = use_case.execute(id)
    if not booking_product:
        logger.info("Booking product %s not found", id)
        raise HTTPException(
            status_code=404, detail={"error": "Booking product not found"}
        )
    session.commit()
    return SummarizeFareRulesResponse(id=booking_product.id, data=booking_product.data)
