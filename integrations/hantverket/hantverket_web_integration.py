import datetime

import pytz
from selenium.webdriver.common.by import By

from booking import Booking
from integration_helper import get_swedish_fake_personal_data
from web_integration import WebIntegration

SWEDISH_MONTH_NAMES = {11: "november", 12: "december", 1: "januari"}


def get_mandatory_extra_parameters():
    return {"email": type("")}


def populate_any_missing_extra_parameters(extra_parameters):
    new_parameters = extra_parameters
    fake_data = get_swedish_fake_personal_data()
    if new_parameters.get("first_name") is None or new_parameters.get("lastname") is None:
        new_parameters["first_name"] = fake_data["first_name"]
        new_parameters["last_name"] = fake_data["last_name"]
    if new_parameters.get("phone") is None:
        new_parameters["phone"] = fake_data["phone"]
    return new_parameters


class HantverketWebIntegration(WebIntegration):

    def attempt_booking(self, restaurant, time, num_persons, extra_parameters):
        super().verify_mandatory_parameters(get_mandatory_extra_parameters(), extra_parameters)
        parameters = populate_any_missing_extra_parameters(extra_parameters)
        web_driver = super().get_web_client()
        web_driver.get("https://restauranghantverket.se/boka-bord")
        super().wait_for_element(self, web_driver, By.XPATH, ".//a[contains(text(), 'Boka bord')]").click()
        web_driver.switch_to.frame(super().wait_for_element(self, web_driver, By.XPATH,
                                                            ".//iframe[contains(@src, 'https://app.waiteraid.com')]"))
        super().wait_for_element(self, web_driver, By.XPATH, ".//li[h3[text() = 'Middag']]").click()
        super().wait_for_element(self, web_driver, By.XPATH,
                                 ".//li[contains(., '" + str(
                                     num_persons) + "') and contains(./span, 'gäster')]").click()
        swedish_time = time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Stockholm'))
        month_swedish_name = SWEDISH_MONTH_NAMES[swedish_time.month]
        super().wait_for_element(self, web_driver, By.XPATH,
                                 ".//div[contains(./div, '"
                                 + month_swedish_name + " " + str(swedish_time.year) +
                                 "') and contains(@class, 'ConsumerCalendar-month')]//div[contains(., '"
                                 + str(swedish_time.day) +
                                 "') and contains(@class, 'ConsumerCalendar-day') and @ng-click and not(contains(@class, 'is-disabled'))]").click()
        super().wait_for_element(self, web_driver, By.XPATH,
                                 ".//li[contains(., '" + str(swedish_time.hour) + ":" + str(
                                     swedish_time.minute) + "')]//a[@class = 'book']").click()
        super().wait_for_element(self, web_driver, By.NAME, "firstname").send_keys(parameters["first_name"])
        web_driver.find_element(By.NAME, "lastname").send_keys(parameters["last_name"])
        valid_mobile_phone = "07" + parameters["phone"][2:]
        web_driver.find_element(By.XPATH, ".//input[@ng-model = 'guestPhone']").send_keys(valid_mobile_phone)
        web_driver.find_element(By.NAME, "email").send_keys(parameters["email"])
        web_driver.find_element(By.XPATH, ".//input[@ng-checked = 'booking.terms.restaurant']").click()
        web_driver.find_element(By.XPATH, ".//button[@ng-click = 'next()']").click()
        # return Booking(restaurant, time, datetime.datetime.utcnow())
        # return None
