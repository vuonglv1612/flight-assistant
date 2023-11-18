from flight_assistant.engine import BookingProductRepository


class ListBookingProductUseCase:
    def __init__(self, booking_products: BookingProductRepository):
        self._booking_products = booking_products

    def execute(self, page: int = 1, page_size: int = 20):
        total, booking_products = self._booking_products.list(page, page_size)
        return {
            "items": booking_products,
            "page": page,
            "page_size": page_size,
            "total": total,
        }
