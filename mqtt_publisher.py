# This the publisher which is publishing the `message` or `payload`  to the Topic defined in config.py.
# This publisher will stop/disconnect once it published the data on broker as its single connection.

import paho.mqtt.publish as publish
from mqtt_project.config import TOPIC, HOSTNAME, PORT

publish.single(topic=TOPIC, hostname=HOSTNAME, port=PORT, payload="test_message")
