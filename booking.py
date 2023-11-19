import json
import datetime


class Booking:
    restaurant: str
    time: datetime.datetime
    created: datetime.datetime

    def __init__(self, restaurant, time, created):
        self.restaurant = restaurant
        self.time = time
        self.created = created

    def __str__(self):
        return f"Booking(restaurant={self.restaurant}, time={self.time}, created={self.created})"

    class BookingEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Booking):
                return {"restaurant": obj.restaurant, "time": str(obj.time), "created": str(obj.created)}
            return super().default(obj)
