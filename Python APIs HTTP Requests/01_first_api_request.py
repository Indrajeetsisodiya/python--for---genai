# Exercise 1 — Your First API Request

# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Import the requests library.
# 2. Send a GET request to the API.
# 3. Store the response in a variable called `response`.
# 4. Print the response.

# Expected output:
# <Response [200]>

# solution


import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response)

# output = <Response [200]>