# MQTT project

## Detailed explanation given in :
https://neetabirajdar.github.io/blog/mqtt_with_example


## MQTT :

MQTT is a great protocal to communicate between multiple devices.

### Example:
There are 2 publishers (light_sensor and temperature_sensor) and they are connected to Broker.
There are multiple subscribers published to the Topics specific to those and they get the data via Broker.

![MQTT broker Connection](/images/example.jpg)


### Used in project:

**MQTT Clients** => Paho Client (https://github.com/eclipse/paho.mqtt.python )

**MQTT Broker** => Mosquitto (https://mosquitto.org )

Broker is running locally so, no code is included for that in this project.
Just the basic Pub/Sub clients are created using `Paho`.
