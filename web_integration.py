from integration import Integration
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium_stealth import stealth


class WebIntegration(Integration):

    def get_web_client(self):
        options = Options()

        options.add_argument("--headless")

        # Create a new Chrome instance
        #TODO not headless, why?
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

    def attempt_booking(self, restaurant, time):
        pass
