# Importing modules
import serial 
import time
import random
from datetime import datetime

# Configure the serial connection to the Arduino
arduino_port = 'COM3'  # Change to your Arduino's serial port
baud_rate = 9600

# Initialize serial connection
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def log_event(event):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {event}")

while True:
    # Generate a random number to send to the Arduino
    blink_count = random.randint(1, 10)
    
    # Send the number to the Arduino
    ser.write(f"{blink_count}\n".encode())
    log_event(f"Sent number to Arduino: {blink_count}")
    
    # Wait for the Arduino to respond with a number
    while ser.in_waiting == 0:
        pass
    
    # Read the number from the Arduino
    wait_time = int(ser.readline().decode().strip())
    log_event(f"Received number from Arduino: {wait_time}")
    
    # Wait for the specified number of seconds
    log_event(f"Sleeping for {wait_time} seconds")
    time.sleep(wait_time)
    log_event("Woke up from sleep")
