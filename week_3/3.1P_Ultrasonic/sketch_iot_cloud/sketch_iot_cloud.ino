#include "thingProperties.h"

// Define the pins for the HC-SR04 sensor
const int trigPin = 11;  // Trigger pin
const int echoPin = 12; // Echo pin

long duration;
float distance;

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500); 

  // Defined in thingProperties.h
  initProperties();

  // Set the HC-SR04 pins as output and input
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  
  /*
     The following function allows you to obtain more information
     related to the state of network and IoT Cloud connection and errors
     the higher number the more granular information you’ll get.
     The default is 0 (only errors).
     Maximum is 4
  */
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
  
  // Your code here 
  // Clear the trigPin by setting it LOW:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Set the trigPin on HIGH state for 10 microseconds:
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, returns the sound wave travel time in microseconds:
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance:
  distance = duration * 0.034 / 2;

  // Print the distance on the Serial Monitor:
  Serial.println("Distance: " + String(distance) + " cm");

  // Update the cloud variable
  distanceMeasurement = distance;
  
  // Delay for 60 seconds (60000 milliseconds)
  delay(30000);
}

/*
  Since distanceMeasurement is READ_WRITE variable, onDistanceMeasurementChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onDistanceMeasurementChange()  {
  // Add your code here to act upon distanceMeasurement change
  Serial.println("--onDistanceMeasurementChange");
}
