from sqlalchemy import JSON, Column
from sqlalchemy.orm import attributes

from .base import Base


class BookingProduct(Base):
    __tablename__ = "booking_product"
    data = Column(JSON, nullable=False)

    def get_fare_rules(self):
        return self.data.get("fare", {}).get("fare_rules", [])

    def update_fare_rules(self, fare_rules):
        self.data["fare"]["fare_rules"] = fare_rules
        attributes.flag_modified(self, "data")
