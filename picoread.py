import serial
import struct
import paho.mqtt.client as mqtt
import json

ser = serial.Serial('/dev/ttyACM0', 115200)
# MQTT broker settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "control"


# MQTT on_connect callback function
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

# MQTT on_message callback function
def on_message(client, userdata, msg):
    try:
        # Convert MQTT message payload to integer
        value = int(msg.payload)
        if value >= 0 and value <= 2:
            # Send value to Arduino over serial
            ser.write(str(value).encode() + b'\n')
            print(f"Sent value {value} to Arduino over serial")
        else:
            print(f"Ignoring invalid value {value} received from MQTT")
    except ValueError:
        print(f"Ignoring non-integer value {msg.payload.decode()} received from MQTT")

# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)

# Start MQTT client loop in background thread
client.loop_start()

# Main loop
while True:
    # Read bytes from serial port until start marker is found
    start_marker = b'\xff\xff'
    while ser.read(2) != start_marker:
        pass

    # Read message body (20 integers)
    message_bytes = ser.read(80)
    message = struct.unpack('20i', message_bytes)

    # Read end marker
    end_marker = ser.read()
    assert end_marker == b'\xfe'

    # Print the received message
    print(message)
    payload = {
        "value1": message[0],
        "value2": message[1],
        "value3": message[2]
    }
    client.publish("ldr", json.dumps(payload))