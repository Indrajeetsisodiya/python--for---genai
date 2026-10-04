# Exercise 13 — Use raise_for_status()

# Use this API:
# https://jsonplaceholder.typicode.com/posts/999999

# This resource does not exist and should return a 404 response.

# Tasks:
# 1. Import the requests library.
# 2. Send a GET request to the API.
# 3. Store the response in `response`.
# 4. Print the status code.
# 5. Call `raise_for_status()` on the response.
# 6. Run the program and observe what happens.

# Do not use try/except yet.
# We will combine raise_for_status() with exception handling
# in the next exercise.

# solution
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
print(response.status_code)
response.raise_for_status()
