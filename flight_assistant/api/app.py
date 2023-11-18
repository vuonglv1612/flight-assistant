from fastapi import FastAPI

from .routes import fare_rules_router

app = FastAPI(title="Flight Assistant API")

app.include_router(
    fare_rules_router, prefix="/booking-products", tags=["Booking Products"]
)
