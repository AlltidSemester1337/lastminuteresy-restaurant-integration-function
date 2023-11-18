from datetime import timedelta

from integration import Integration
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium_stealth import stealth


class WebIntegration(Integration):

    def get_web_client(self):
        options = Options()

        options.add_argument("--headless")

        # Create a new Chrome instance
        driver = webdriver.Chrome(options=options)
        stealth(driver,

                languages=["en-US", "en"],

                vendor="Google Inc.",

                platform="Win32",

                webgl_vendor="Intel Inc.",

                renderer="Intel Iris OpenGL Engine",

                fix_hairline=True,

                )
        return driver

    def attempt_booking(self, restaurant, time, extra_parameters):
        pass

    @staticmethod
    def wait_for_element(self, web_driver, by, selector, wait):
        timeout = wait
        if not timeout:
            timeout = timedelta(10)
        #TODO continue here!
        element = web_driver.find_element(by, selector)
        # free_tables is not None and int(free_tables.split(": ")[1]) < 1:
        #    return None
        #else:
        #    web_driver.find_element(By.TAG_NAME, "a").click()
        #    start = datetime.datetime.utcnow()
        #    while datetime.datetime.utcnow() < start + datetime.timedelta(seconds=5):
        #        booking_message = web_driver.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
        #        if booking_message is not None and super().BOOK_SUCCESS_MESSAGE in booking_message.casefold():
        #            return Booking(restaurant, time, datetime.datetime.utcnow())
        #        t.sleep(1)
        return None