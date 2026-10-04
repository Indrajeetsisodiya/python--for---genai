# Exercise 7 — Handle a Failed API Request

# Use this API:
# https://jsonplaceholder.typicode.com/posts/999999

# This resource does not exist.

# Tasks:
# 1. Import the requests library.
# 2. Send a GET request to the API.
# 3. Store the response in a variable called `response`.
# 4. Check whether the status code is 404.
# 5. If it is 404, print:
#    Resource not found
# 6. Otherwise, print:
#    Request successful

# solution
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
print(response.status_code)
if response.status_code == 404:
    print("Resource not found")
else:
    print("Request successful")
