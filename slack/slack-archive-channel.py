# Import necessary libraries
import requests
import json

# Define constants
CHANNEL_ID="CHANNEL_ID"
URL = "https://slack.com/api/conversations.archive"
TOKEN = "TOKEN"

# Function to archive a channel
def archive_channel(CHANNEL_ID):
    # Define headers and data for the API request
    headers = {}
    data = {
        "token": TOKEN,
        "channel": CHANNEL_ID
    }
    try:
        # Make a POST request to the API
        response = requests.post(URL, json=data)
        # If the response indicates an error, raise an exception
        response.raise_for_status()
        # Get the status code and response body
        status = response.status_code
        dictionary = response.json()
        # Print the status code, channel ID, and response body
        print(f"{status} {CHANNEL_ID} {dictionary}")
    # If an error occurred while making the request, print it
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

# Main function to call the archive_channel function
def main():
  archive_channel(CHANNEL_ID)

# If this script is run (not imported), call the main function
if __name__ == "__main__":
    main()