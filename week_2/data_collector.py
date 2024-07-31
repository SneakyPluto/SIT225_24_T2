import serial
import time
import csv
from datetime import datetime

# Set up the serial connection (make sure to adjust the port name and baud rate as needed)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate port for your setup

# Open CSV file to write data
with open('dht22_data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    while True:
        try:
            # Read data from serial port
            data = ser.readline().decode().strip()
            # Get current timestamp
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            # Split data into temperature and humidity
            temperature, humidity = data.split(',')
            # Write data to CSV file
            writer.writerow([timestamp, temperature, humidity])
            # Wait for the next sample
            time.sleep(60)  # 60 seconds interval
        except KeyboardInterrupt:
            print("Data collection stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
print('Data collection completed.')