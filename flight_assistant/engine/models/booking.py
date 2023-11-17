from sqlalchemy import (
    ForeignKey,
    Float,
    Integer,
    Column,
    String,
    JSON,
    Boolean,
    TIMESTAMP,
    ARRAY,
    Text,
)


class BookingProduct(BaseModel):
    data = Column(JSON, nullable=False)
