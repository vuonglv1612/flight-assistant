from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from flight_assistant.engine.models import BookingProduct


class BookingProductRepository(ABC):
    @abstractmethod
    def list(self, page: int = 1, page_size: int = 20):
        pass

    @abstractmethod
    def find_by_id(self, booking_product_id: str):
        pass

    @abstractmethod
    def save(self, booking_product):
        pass


class SQLAlchemyBookingProductRepository(BookingProductRepository):
    def __init__(self, pg_session: Session):
        self._session = pg_session

    def find_by_id(self, booking_product_id: str):
        booking_product = self._session.query(BookingProduct).get(booking_product_id)
        return booking_product

    def save(self, booking_product):
        self._session.add(booking_product)

    def list(self, page: int = 1, page_size: int = 20):
        total = self._session.query(BookingProduct).count()
        booking_products = (
            self._session.query(BookingProduct)
            .limit(page_size)
            .offset((page - 1) * page_size)
        )
        return total, booking_products.all()
