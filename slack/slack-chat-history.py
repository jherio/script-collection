# Import necessary libraries
import requests
import json

# Function to fetch chat history of a channel
def chatHistory(channel_id, next_cursor):
    # Define headers and data for the API request
    headers = {}
    data = {
        "token": "TOKEN", # Replace TOKEN with your Slack API token
        "channel": channel_id # Replace CHANNEL_ID with the channel ID
    }
    # Make a POST request to the Slack API to fetch the chat history
    history_request = requests.post("https://slack.com/api/conversations.history", headers=headers, json=data)
    # Get the status code and response body
    status = history_request.status_code
    dictionary = history_request.json()
    try:
        # Try to get the next cursor from the response
        next_cursor = dictionary["response_metadata"]["next_cursor"]
    except KeyError:
        # If there's no next cursor, print "No more messages"
        print("No more messages")

    # Convert the response body to a pretty formatted JSON string
    pretty_json = json.dumps(dictionary, indent=2)
    # Write the pretty JSON string to a file
    with open(f"channel_{channel_id}_history.json", "a") as f:
        f.write(pretty_json)

# Function to read a list of channel IDs from a file
def readChannels(filename):
    with open(filename, "r") as f:
        # Read the file line by line, strip whitespace from each line, and return the list of lines
        channels = [line.strip() for line in f]
    return channels

# Main function
def main():
    # For each channel ID in the list read from "list_of_channels", fetch the chat history
    for channel_id in readChannels("list_of_channels"):
        chatHistory(channel_id, "NEXT_CURSOR") # Replace "NEXT_CURSOR" with your actual cursor

# If this script is run (not imported), call the main function
if __name__ == "__main__":
    main()