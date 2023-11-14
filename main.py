import base64
import datetime

import functions_framework
from google.cloud import pubsub_v1
import json

from booking import Booking
from integrations.demo import demo_restaurant_api_integration, demo_restaurant_web_integration

# TODO Consider one function per integration?

INTEGRATIONS = {1: demo_restaurant_api_integration.DemoRestaurantApiIntegration(),
                2: demo_restaurant_web_integration.DemoRestaurantWebIntegration()}

project_id = "sapient-bucksaw-401016"
topic_id = "bookings"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)


def publish_new_booking(new_booking):
    new_booking_str = json.dumps(new_booking, cls=Booking.BookingEncoder)
    new_booking_data = new_booking_str.encode("utf-8")
    print(f"Publish {new_booking_data}.")
    future = publisher.publish(topic_path, new_booking_data)
    future.result()


class BookingFailedException(Exception):
    pass


@functions_framework.cloud_event
def handle_incoming_booking_request_event(cloud_event):
    print(f"Handling {cloud_event}.")
    event_data = cloud_event.get_data()["message"]["data"]
    booking_request = json.loads(base64.b64decode(event_data))
    requested_booking_time = datetime.datetime.fromisoformat(booking_request["time"])
    integration = INTEGRATIONS[booking_request["integration_id"]]
    new_booking = integration.attempt_booking(booking_request["restaurant"], requested_booking_time)
    if new_booking is not None:
        publish_new_booking(new_booking)
    else:
        raise BookingFailedException()
