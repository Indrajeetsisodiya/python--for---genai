# Exercise 4 — Basic API Error Checking

# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Import the requests library.
# 2. Send a GET request to the API.
# 3. Check whether the status code is 200.
# 4. If the status code is 200, print:
#    Request successful
# 5. Otherwise, print:
#    Request failed

# solution
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("request successful")
else:
    print("request failed")
