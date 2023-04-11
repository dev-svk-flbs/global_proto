import json
import paho.mqtt.client as mqtt
from celery import Celery
from datetime import datetime, timezone, timedelta
import os
import django
import time

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globalsite.settings')

# Initialize Django app
django.setup()

from tof.models import TofData, TofData1, TofData2, VizData, LdrData
from tof.tasks import process_data, create_incident

# MQTT broker settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPICS = [("tof", TofData), ("tof1", TofData1), ("tof2", TofData2), ("viz", VizData), ("ldr", LdrData) ]

# Initialize Celery instance
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Initialize message count and timestamp for each topic
message_counts = {topic: 0 for topic, _ in MQTT_TOPICS}
last_message_times = {topic: time.time() for topic, _ in MQTT_TOPICS}


# Define a flag to indicate if we are currently in an incident state
incident_state = False

# Define a timestamp to indicate when the incident state started
incident_start_time = None

# Define a time interval to disable incident reporting after an incident is detected
incident_disable_interval = timedelta(seconds=5)


# Define callback function for when a message is received
def on_message(client, userdata, message):
    global incident_state
    global incident_start_time

    # Parse payload and timestamp
    payload = json.loads(message.payload)
    timestamp = datetime.utcfromtimestamp(message.timestamp).replace(tzinfo=timezone.utc)

    # Determine which topic the message was received on
    for topic, model in MQTT_TOPICS:
        
        if message.topic == topic:
            if payload.get('value1') == 1:
                client.publish("control", "1")
            # Check if we are currently in an incident state
            if incident_state:
                # Check if the incident disable interval has elapsed
                if datetime.now(timezone.utc) >= incident_start_time + incident_disable_interval:
                    # Disable the incident state
                    incident_state = False
                    incident_start_time = None
                else:
                    # We are still in the incident state, ignore the current message
                    pass
            else:
                # Check if the current value1 is 2, i.e., break!!!!!
                if payload.get('value1') == 2:
                    # Set the incident state flag and start the incident disable interval
                    print("-------------------------------------------------------------")
                    incident_state = True
                    incident_start_time = datetime.now(timezone.utc)
                    
                    # Send the brake signal (placeholder code)
                    print("Brake signal sent")
                    client.publish("control", "2")
                    
                    # Call the create_incident function through Celery
                    create_incident.delay(timestamp)
                    
            # Send the data to Celery for processing with the appropriate model
            if time.time() - last_message_times[topic] > 0.33:
                process_data.delay(timestamp, payload, topic)
                last_message_times[topic] = time.time()
            break
    print(topic, payload)

# Create MQTT client instance
client = mqtt.Client()

# Set callback function
client.on_message = on_message

# Connect to MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

# Subscribe to MQTT topics
for topic, _ in MQTT_TOPICS:
    client.subscribe(topic)

# Start the MQTT loop
client.loop_forever()
