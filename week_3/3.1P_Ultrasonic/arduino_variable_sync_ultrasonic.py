import sys
import traceback
import random
from arduino_iot_cloud import ArduinoCloudClient
import asyncio
import time

DEVICE_ID = "762d7372-1b9c-4b55-bf2e-c848371b5a4f"
SECRET_KEY = "HWYKCHRbxhwarYVPaIQs?Ys2x"

# Open the file in append mode
file = open('distance_data.csv', 'a')

# Callback function on distance change event. Write function used to pass the csv as a string
def on_distance_changed(client, value):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    csv_string = f"{timestamp},{value}\n"
    file.write(csv_string)
    file.flush()  # Ensure data is written to the file immediately

async def fetch_distance(client):
    while True:
        await asyncio.sleep(60)  # Fetch data every 60 seconds
        distance = client.get_variable("distanceMeasurement")
        print(f"Fetched distance: {distance}")

def main():
    print("main() function")

    # Instantiate Arduino cloud client
    client = ArduinoCloudClient(
        device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY
    )

    # Register with 'distanceMeasurement' cloud variable
    # and listen on its value changes in 'on_distance_changed'
    # callback function.
    client.register(
        "distanceMeasurement", value=None, 
        on_write=on_distance_changed)

    # start cloud client
    client.start()

    # Create and run the asyncio event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_distance(client))

if __name__ == "__main__":
    try:
        main()  # main function which runs in an internal infinite loop
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_type, file=print)
    finally:
        file.close()  # Ensure the file is closed at the end of execution
