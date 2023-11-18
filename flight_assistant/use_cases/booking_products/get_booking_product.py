from flight_assistant.engine import BookingProductRepository


class GetBookingProductUseCase:
    def __init__(self, booking_products: BookingProductRepository):
        self._booking_products = booking_products

    def execute(self, booking_product_id: str):
        booking_product = self._booking_products.find_by_id(booking_product_id)
        return booking_product
