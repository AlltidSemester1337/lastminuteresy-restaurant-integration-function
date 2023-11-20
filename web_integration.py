import time
from datetime import timedelta, datetime

from selenium.common import NoSuchElementException

from integration import Integration
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium_stealth import stealth


class WebIntegration(Integration):

    def get_web_client(self):
        options = Options()

        # TODO REVERT BEFORE DEPLOY
        # options.add_argument("--headless")

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

    def attempt_booking(self, restaurant, time, num_persons, extra_parameters):
        pass

    @staticmethod
    def wait_for_element(self, web_driver, by, selector, wait=None):
        timeout = wait
        if not timeout:
            timeout = timedelta(10)

        end = datetime.utcnow() + timeout
        while datetime.utcnow() < end:
            try:
                element = web_driver.find_element(by, selector)
                if element is not None:
                    return element
                else:
                    time.sleep(1)
            except NoSuchElementException as e:
                time.sleep(1)
        return None
