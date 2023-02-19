# This the subscriber which is subscribed to the Topic defined in config.py and is listening to the message coming on that topic.
# You can give any `client_id` when you are running locally instead of `test_client`.
# Using `qos=0`, which means we want the message atmost once.

import paho.mqtt.subscribe as susbcribe
from mqtt_project.config import TOPIC, HOSTNAME, PORT

message = susbcribe.simple(
    topics=TOPIC, hostname=HOSTNAME, port=PORT, client_id="test_client", qos=0
)

print(f"\nTopic: {message.topic}")
print(f"\nMessage: {message.payload}")
