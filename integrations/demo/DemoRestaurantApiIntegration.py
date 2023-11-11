import datetime

from booking import Booking
import ApiIntegration
import AbstractDemoRestaurantIntegration


class DemoRestaurantApiIntegration(ApiIntegration, AbstractDemoRestaurantIntegration):
    def attempt_booking(self, restaurant, time):
        booking_response = requests.get(super().book_endpoint_url)
        if booking_response.status == 200 and booking_response.content.casefold().contains(super().book_success_message):
            return Booking(restaurant, time, datetime.datetime.utcnow())
        return None
