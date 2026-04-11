import json
import time
from google.cloud import pubsub_v1

project_id = "project-93921294-15bc-440f-acb"
topic_id = "weather-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_message():
    data = {
        "city": "Dublin",
        "temperature": 15,
        "timestamp": time.time()
    }
    message_json = json.dumps(data)
    message_bytes = message_json.encode("utf-8")

    future = publisher.publish(topic_path, message_bytes)
    print(f"Published message ID: {future.result()}")

while True:
    publish_message()
    time.sleep(5)