# get.py
# CS2104 Week 9 - HTTP GET example
# Author: Ushnah Khan

import requests  # allows us to make HTTP requests

# 1. Ask the user for the Webhook.site "Raw" URL
url = input("Enter your unique URL from webhook.site: ")

# 2. Make the GET request
response = requests.get(url)

# 3. Convert the response into JSON (Python dictionary)
data = response.json()

# 4. Print the full JSON response (for debugging / verification)
print("Full JSON response:", data)

# 5. Print only the key-value pair containing your message
#    (adjust 'name' to match whatever key you used when posting)
print("Message:", data["name"])
