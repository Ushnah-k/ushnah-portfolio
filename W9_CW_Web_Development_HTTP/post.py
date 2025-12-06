# post.py
# CS2104 Week 9 - HTTP POST example
# Author: Ushnah Khan

import requests  # library for making HTTP requests

# 1. Ask user for a message
message = input("Enter a message to send: ")

# 2. Create the JSON object to send (key = 'name' or any label you like)
data = {"name": message}

# 3. Your Webhook.site URL (Inbox URL)
url = "https://webhook.site/467b5147-3722-4bce-b8de-c4d1cd2878c0"  # <-- replace with your unique URL if needed

# 4. Make the POST request
response = requests.post(url, json=data)

# 5. Print confirmation
print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Message sent successfully!")
