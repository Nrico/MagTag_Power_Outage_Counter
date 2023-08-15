import board
import time
from adafruit_magtag.magtag import MagTag
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError
import secrets  # Import the secrets file

# Initialize MagTag
magtag = MagTag()

# Connect to WiFi
magtag.network.connect()

# Adafruit IO credentials from secrets.py
ADAFRUIT_IO_USER = secrets.secrets['aio_username']
ADAFRUIT_IO_KEY = secrets.secrets['aio_key']
FEED_NAME = 'power-outage-counter'

# Initialize Adafruit IO with the requests session from MagTag's network manager
io = IO_HTTP(ADAFRUIT_IO_USER, ADAFRUIT_IO_KEY, magtag.network.requests)

def get_power_outage_count():
    """Retrieve the power outage count from Adafruit IO."""
    try:
        feed = io.get_feed(FEED_NAME)
        value = io.receive_data(feed["key"])
        return int(value["value"])
    except AdafruitIO_RequestError:
        # If feed doesn't exist, create it and initialize with 0
        io.create_new_feed(FEED_NAME)
        io.send_data(FEED_NAME, 0)
        return 0

def update_power_outage_count(count):
    """Update the power outage count on Adafruit IO."""
    io.send_data(FEED_NAME, count)
    
    # Add text with a specified position
text_area = magtag.add_text(
    text_position=(20, 20),  # 20 pixels down and 20 pixels to the side
    text_scale=2
)

def main():
    # Get the current power outage count
    count = get_power_outage_count()

    # Increment the count
    count += 1

    # Update the count on Adafruit IO
    update_power_outage_count(count)
    
    # Display the count on the MagTag
    text_to_display = f"Power Outages: {count}"
    magtag.set_text(text_to_display)

    while True:
        # Sleep to prevent excessive queries and updates
        time.sleep(60)

if __name__ == "__main__":
    main()
