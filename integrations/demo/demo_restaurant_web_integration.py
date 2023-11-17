import datetime

from selenium.webdriver.common.by import By

from booking import Booking
from web_integration import WebIntegration
from integrations.demo.demo_restaurant_integration import DemoRestaurantIntegration
import time as t


class DemoRestaurantWebIntegration(WebIntegration, DemoRestaurantIntegration):
    def attempt_booking(self, restaurant, time):
        web_driver = super().get_web_client()
        print(web_driver)
        web_driver.get(super().BOOK_HOME_ENDPOINT_URL)
        t.sleep(1)
        free_tables = web_driver.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
        if free_tables is not None and int(free_tables.split(": ")[1]) < 1:
            return None
        else:
            web_driver.find_element(By.TAG_NAME, "a").click()
            start = datetime.datetime.utcnow()
            while datetime.datetime.utcnow() < start + datetime.timedelta(seconds=5):
                booking_message = web_driver.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
                if booking_message is not None and super().BOOK_SUCCESS_MESSAGE in booking_message.casefold():
                    return Booking(restaurant, time, datetime.datetime.utcnow())
                t.sleep(1)
        return None
