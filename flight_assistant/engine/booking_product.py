from abc import ABC, abstractmethod

from sqlalchemy.orm import Session
from .models import BookingProduct


class BookingProductRepository(ABC):
    @abstractmethod
    def find_by_id(self, booking_product_id: str):
        pass

    @abstractmethod
    def save(self, booking_product):
        pass


class PostgresFareRuleClient(BookingProductRepository):
    def __init__(self, pg_session: Session):
        self._session = pg_session

    def find_by_id(self, booking_product_id: str):
        booking_product = self._session.query(BookingProduct).get(booking_product_id)
        return booking_product

    def save(self, booking_product):
        self._session.add(booking_product)
