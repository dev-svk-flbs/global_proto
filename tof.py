import time
import paho.mqtt.client as mqtt
import json
import random

# MQTT broker settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "tof"

# Create MQTT client instance
client = mqtt.Client()

# Connect to MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

# Define function to read value1 from file
def read_value1():
    with open('value1.txt', 'r') as f:
        return int(f.read().strip())

# Publish values from file
while True:
    payload = {
        "value1": read_value1(),
        "value2": random.randint(0, 10),
        "value3": random.randint(0, 20)
    }
    client.publish(MQTT_TOPIC, json.dumps(payload))
    print("Published payload:", payload)
    time.sleep(.03)
