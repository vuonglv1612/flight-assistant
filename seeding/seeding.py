import json

import config
from flight_assistant.engine.connection import create_session_factory
from flight_assistant.engine.models import BookingProduct


def run(file_name):
    with open(file_name) as f:
        rules = json.load(f)

    session = create_session_factory(config.ENGINE_POSTGRES_URI)()
    for rule in rules:
        booking_product = BookingProduct(data=rule["data"])
        session.add(booking_product)
    session.commit()
    print("Added {} booking products".format(len(rules)))
