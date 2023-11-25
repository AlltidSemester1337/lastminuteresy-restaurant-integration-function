import base64
import datetime

import functions_framework
from google.cloud import pubsub_v1
import json

from booking import Booking
from integrations.demo import demo_restaurant_api_integration, demo_restaurant_web_integration
from integrations.hantverket import hantverket_web_integration
from model.booking_failed_exception import BookingFailedException

INTEGRATIONS = {1: demo_restaurant_api_integration.DemoRestaurantApiIntegration(),
                2: demo_restaurant_web_integration.DemoRestaurantWebIntegration(),
                3: hantverket_web_integration.HantverketWebIntegration()}

project_id = "sapient-bucksaw-401016"
topic_id = "bookings"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)


def publish_new_booking(new_booking):
    new_booking_str = json.dumps(new_booking, cls=Booking.BookingEncoder)
    new_booking_data = new_booking_str.encode("utf-8")
    print(f"Publish {new_booking_data}.")
    future = publisher.publish(topic_path, new_booking_data)
    future.result()


@functions_framework.cloud_event
def handle_incoming_booking_request_event(cloud_event):
    print(f"Handling {cloud_event}.")
    event_data = cloud_event.get_data()["message"]["data"]
    booking_request = json.loads(base64.b64decode(event_data))
    requested_booking_time = datetime.datetime.fromisoformat(booking_request["time"])

    integration = INTEGRATIONS[booking_request["integration_id"]]
    new_booking = integration.attempt_booking(booking_request["restaurant"], requested_booking_time,
                                              booking_request["num_persons"],
                                              booking_request["extra_parameters"])

    if new_booking is not None:
        publish_new_booking(new_booking)
    else:
        raise BookingFailedException()
