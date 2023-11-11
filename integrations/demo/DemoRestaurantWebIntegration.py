import datetime

from booking import Booking
import WebIntegration
import AbstractDemoRestaurantIntegration


class DemoRestaurantWebIntegration(WebIntegration, AbstractDemoRestaurantIntegration):
    def attempt_booking(self, restaurant, time):
        web_client = super().get_web_client()
        #TODO fix
        booking_response = web_client.get(super().book_endpoint_url)
        if booking_response.body.textContent.casefold().contains(super().book_success_message):
            return Booking(restaurant, time, datetime.datetime.utcnow())
        return None
