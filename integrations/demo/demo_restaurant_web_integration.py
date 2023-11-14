import datetime

from booking import Booking
from web_integration import WebIntegration
from integrations.demo.demo_restaurant_integration import DemoRestaurantIntegration


class DemoRestaurantWebIntegration(WebIntegration):
    def attempt_booking(self, restaurant, time):
        # web_client = super().get_web_client()
        # TODO fix
        # booking_response = web_client.get(BOOK_ENDPOINT_URL)
        # if BOOK_SUCCESS_MESSAGE in booking_response.body.textContent.casefold():
        #    return Booking(restaurant, time, datetime.datetime.utcnow())
        return None
