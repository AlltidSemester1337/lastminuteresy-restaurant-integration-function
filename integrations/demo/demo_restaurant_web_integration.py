import datetime

from selenium.webdriver.common.by import By

from booking import Booking
from web_integration import WebIntegration
from integrations.demo.demo_restaurant_integration import DemoRestaurantIntegration
import time as t


class DemoRestaurantWebIntegration(WebIntegration, DemoRestaurantIntegration):
    def attempt_booking(self, restaurant, time, num_persons, extra_parameters):
        web_driver = super().get_web_client()
        web_driver.get(super().BOOK_HOME_ENDPOINT_URL)
        free_tables = super().wait_for_element(self, web_driver, By.TAG_NAME, "strong").get_attribute("textContent")
        if int(free_tables.split(": ")[1]) < 1:
            return None
        else:
            web_driver.find_element(By.TAG_NAME, "a").click()
            booking_message = super().wait_for_element(self, web_driver, By.TAG_NAME, "strong").get_attribute(
                "textContent")
            if super().BOOK_SUCCESS_MESSAGE in booking_message.casefold():
                return Booking(restaurant, time, datetime.datetime.utcnow())
            return None
