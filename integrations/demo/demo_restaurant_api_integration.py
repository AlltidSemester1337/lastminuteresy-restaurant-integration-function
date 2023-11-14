import datetime

from booking import Booking
from api_integration import ApiIntegration
from integrations.demo.demo_restaurant_integration import DemoRestaurantIntegration
import requests


class DemoRestaurantApiIntegration(ApiIntegration, DemoRestaurantIntegration):

    def attempt_booking(self, restaurant, time):
        booking_response = requests.get(super().BOOK_ENDPOINT_URL)
        if booking_response.ok and super().BOOK_SUCCESS_MESSAGE in booking_response.content.decode('utf-8').casefold():
            return Booking(restaurant, time, datetime.datetime.utcnow())
        return None
