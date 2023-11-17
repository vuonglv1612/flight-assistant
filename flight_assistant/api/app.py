from fastapi import FastAPI
from .routes import fare_rules_router

app = FastAPI()

app.include_router(fare_rules_router)
