# Exercise 3 — Check the API Status Code

# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Import the requests library.
# 2. Send a GET request to the API.
# 3. Store the response in a variable called `response`.
# 4. Print the HTTP status code.

# Expected output:
# 200

# solution
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)

# output = 200