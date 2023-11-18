class DemoRestaurantIntegration:
    BOOK_ENDPOINT_URL = "http://35.233.70.88:8080/demorestaurant/book"
    BOOK_HOME_ENDPOINT_URL = "http://35.233.70.88:8080/demorestaurant/bookTable.html"
    BOOK_SUCCESS_MESSAGE = "table booked!"

    def get_mandatory_extra_parameters(self):
        return {"email": type("")}
