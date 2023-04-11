import random
import time
import paho.mqtt.client as mqtt
import json

# MQTT broker settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "ldr"

# Create MQTT client instance
client = mqtt.Client()

# Connect to MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

# Generate and publish random values
while True:
    payload = {
        "value1": random.randint(0, 1),
        "value2": random.randint(0, 10),
        "value3": random.randint(0, 20)
    }
    client.publish(MQTT_TOPIC, json.dumps(payload))
    print("Published payload:", payload)
    time.sleep(.03)
