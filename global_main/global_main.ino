// Define the array and initialize to 0
int myArray[20] = {0};

// Variables to keep track of the time elapsed since last execution
unsigned long lastObtainTime = 0;
const unsigned long obtainInterval = 50; // Interval between obtaining items in milliseconds

void setup() {
  // Start serial communication at 115200 baud
  Serial.begin(115200);
  // Initialize RGB LED pins as outputs
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
}

void loop() {
  // Check if it's time to obtain items again
  unsigned long currentTime = millis();
  if (currentTime - lastObtainTime >= obtainInterval) {
    // Obtain random values between 0 and 10000 for items 4-13 and store them in the array
    for (int i = 3; i <= 12; i++) {
      myArray[i] = random(0, 10001);
    }

    // Update the last obtain time
    lastObtainTime = currentTime;
  }

  // Generate random detection result of 0, 1, or 2 for item 1
  myArray[0] = random(0, 3);

  // Set items 2-11 to random values between 0 and 10000
  for (int i = 1; i <= 10; i++) {
    myArray[i + 1] = random(0, 10001);
  }

  // Set the remaining items to 0
  for (int i = 13; i < 20; i++) {
    myArray[i] = 0;
  }

  // Send the entire array as a single message with predetermined start and end markers via serial
  Serial.write(0xFF);
  Serial.write(0xFF);
  Serial.write((byte*)&myArray, sizeof(myArray));
  Serial.write(0xFE);


  // Check if there is data available to read
  if (Serial.available() > 0) {
    // Read the data until a newline is received
    String message = "";
    while (Serial.available() > 0) {
      char incomingByte = Serial.read();
      message += incomingByte;
      if (incomingByte == '\n') {
        // Process the received message
        if (message == "0\n") {
          digitalWrite(25, HIGH);
          digitalWrite(26, LOW);
          digitalWrite(27, LOW);
        } else if (message == "1\n") {
          digitalWrite(25, LOW);
          digitalWrite(26, HIGH);
          digitalWrite(27, LOW);
        } else if (message == "2\n") {
          digitalWrite(25, LOW);
          digitalWrite(26, LOW);
          digitalWrite(27, HIGH);
        }
        // Reset the message buffer
        message = "";
      }
    }
  }


  // Wait for 20 milliseconds (50 times per second)
  delay(20);
}
