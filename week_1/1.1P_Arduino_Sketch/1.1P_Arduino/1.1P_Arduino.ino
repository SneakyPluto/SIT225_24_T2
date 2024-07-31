void setup() {
  // Initialize the digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  // Start serial communication at 9600 baud rate
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming number
    int blinkCount = Serial.parseInt();
    
    // Blink the LED 'blinkCount' times
    for (int i = 0; i < blinkCount; i++) {
      digitalWrite(LED_BUILTIN, HIGH);   // Turn the LED on (HIGH is the voltage level)
      delay(1000);                  // Wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // Turn the LED off by making the voltage LOW
      delay(1000);                  // Wait for a second+
    }
    
    // Generate a random number to send back to the Python script
    int waitTime = random(1, 10);
    
    // Send the number back to the Python script
    Serial.println(waitTime);
  }
}
