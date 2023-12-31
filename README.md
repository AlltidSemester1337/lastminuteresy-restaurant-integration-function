<h1>Lastminuteresy restaurant-integration-function</h1>

<p>
Serverless gcloud function to attempt and return (publish) potential restaurant booking from request on pub/sub topic
</p>

<h2>Run locally</h2>
<p>
pip install -r requirements.txt
functions-framework --target=handle_incoming_booking_request_event --signature-type=cloudevent
</p>

<p>Test for example via curl:
<code>
curl localhost:8080 \
  -X POST \
  -H "Content-Type: application/json" \
  -H "ce-id: 123451234512345" \
  -H "ce-specversion: 1.0" \
  -H "ce-time: 2020-01-02T12:34:56.789Z" \
  -H "ce-type: google.cloud.pubsub.topic.v1.messagePublished" \
  -H "ce-source: //pubsub.googleapis.com/projects/sapient-bucksaw-401016/topics/booking-requests" \
  -d '{
        "message": {
          "data": "eyJpbnRlZ3JhdGlvbl9pZCI6IDEsICJyZXN0YXVyYW50IjogImRlbW9yZXN0YXVyYW50IiwgInRpbWUiOiAiMjAyMy0xMS0xNSAxMjozMDowMCIsICJjcmVhdGVkIjogIjIwMjMtMTEtMTQgMTE6Mzg6MjEuNTQxNDgwIn0="
        },
        "subscription": "projects/sapient-bucksaw-401016/subscriptions/booking-requests-sub"
      }'
</code>
</p>

<h2>Deploy process</h2>
<p>requirements.txt updated and gcloud auth / credentials configured</p>
<ul>
<li>deploy function <br>
gcloud functions deploy restaurant_integrations \
--gen2 \
--region=europe-west1 \
--runtime=python312 \
--source=https://source.developers.google.com/projects/sapient-bucksaw-401016/repos/github_alltidsemester1337_lastminuteresy-restaurant-integration-function/revisions/main \
--entry-point=handle_incoming_booking_request_event \
--trigger-topic=booking-requests \
--max-instances=5
</li>
<li>confirm by reading logs:
gcloud functions logs read restaurant_integrations --region europe-west1
</li>
</ul>
