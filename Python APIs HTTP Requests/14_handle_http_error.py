# Exercise 14 — Handle an HTTP Error

# Use this API:
# https://jsonplaceholder.typicode.com/posts/999999

# This resource does not exist.

# Tasks:
# 1. Send a GET request to the API.
# 2. Store the response in `response`.
# 3. Use `raise_for_status()` to check for an HTTP error.
# 4. Use try/except to catch `requests.exceptions.HTTPError`.
# 5. If an HTTPError occurs, print:
#    API request failed
# 6. After the try/except block, print:
#    Program continues

# Expected output:
# API request failed
# Program continues

# solution
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
try:
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("API  request failed")

print("program continues")
