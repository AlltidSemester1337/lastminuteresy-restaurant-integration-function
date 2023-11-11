import base64
import datetime

import functions_framework
from google.cloud import pubsub_v1
import json

from booking import Booking
from integrations.demo.DemoRestaurantApiIntegration import DemoRestaurantApiIntegration
from integrations.demo.DemoRestaurantWebIntegration import DemoRestaurantWebIntegration

# TODO Consider one function per integration?
# TODO: how to schedule retries?

# TODO update tableservice to use ID instead of restaurant name, in case we have multiple integrations for the same restaurant
#TODO Also perhaps this should be moved to a separate service so there is no redundancy and risk of inconsistency in ID mappings,
# but that can be a future version
INTEGRATIONS = {1: DemoRestaurantApiIntegration(), 2: DemoRestaurantWebIntegration()}

project_id = "sapient-bucksaw-401016"
topic_id = "bookings"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)


def publish_new_booking(new_booking):
    new_booking_str = json.dumps(new_booking, cls=Booking.BookingEncoder)
    new_booking_data = new_booking_str.encode("utf-8")
    future = publisher.publish(topic_path, new_booking_data)
    future.result()


# TODO Might not be correct way, check this
@functions_framework.event
def init(event, context):
    booking_request = json.loads(base64.b64decode(event["data"]))
    requested_booking_time = datetime.datetime.fromisoformat(booking_request["time"])
    integration = INTEGRATIONS[booking_request["integration_id"]]
    new_booking = integration.attempt_booking(booking_request["restaurant"], requested_booking_time)
    if new_booking is not None:
        publish_new_booking(new_booking)
