import datetime

import pytz
from selenium.webdriver.common.by import By

from booking import Booking
from web_integration import WebIntegration
import time as t

SWEDISH_MONTH_NAMES = {11: "november", 12: "december", 1: "januari"}


def get_mandatory_extra_parameters():
    return {"email": type("")}


class HantverketWebIntegration(WebIntegration):

    def attempt_booking(self, restaurant, time, num_persons, extra_parameters):
        super().verify_mandatory_parameters(get_mandatory_extra_parameters(), extra_parameters)
        web_driver = super().get_web_client()
        web_driver.get("https://restauranghantverket.se/boka-bord")
        super().wait_for_element(self, web_driver, By.XPATH, ".//a[contains(text(), 'Boka bord')]").click()
        super().wait_for_element(self, web_driver, By.XPATH, ".//li[h3[text() = 'Middag']]").click()
        super().wait_for_element(self, web_driver, By.XPATH,
                                 ".//li[contains(., '" + num_persons + "') and contains(./span, 'gäster')]").click()
        swedish_time = time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Stockholm'))
        month_swedish_name = SWEDISH_MONTH_NAMES[swedish_time.month]
        super().wait_for_element(self, web_driver, By.XPATH,
                                 ".//div[contains(./div, '"
                                 + month_swedish_name + " " + swedish_time.year +
                                 "') and contains(@class, 'ConsumerCalendar-month')]//div[contains(., '"
                                 + swedish_time.day_of_month +
                                 "') and contains(@class, 'ConsumerCalendar-day') and @ng-click and not(contains(@class, 'is-disabled'))]").click()
        super().wait_for_element(self, web_driver, By.XPATH,
                                 ".//li[contains(., '" + swedish_time.hour + ":" + swedish_time.minute + "')]//a[@class = 'book']").click()
        #TODO ENter input text, continue from contact form page
        #super().wait_for_element(self, web_driver, By.NAME, "firstname")
        #return Booking(restaurant, time, datetime.datetime.utcnow())
        #return None
