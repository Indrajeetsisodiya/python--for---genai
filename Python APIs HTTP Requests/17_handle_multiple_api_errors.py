# Exercise 17 — Handle Multiple API Errors

# Use this URL:
# https://jsonplaceholder.typicode.com/posts/999999

# This API request should return a 404 response.

# Tasks:
# 1. Send the GET request inside a try block.
# 2. Set a timeout of 5 seconds.
# 3. Call raise_for_status().
# 4. Catch requests.exceptions.ConnectionError.
# 5. Catch requests.exceptions.Timeout.
# 6. Catch requests.exceptions.HTTPError.
# 7. For ConnectionError, print:
#    Could not connect to the API
# 8. For Timeout, print:
#    Request timed out
# 9. For HTTPError, print:
#    API returned an HTTP error
# 10. After the try/except blocks, print:
#     Program continues

# Expected output:
# API returned an HTTP error
# Program continues

# solution
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/999999",timeout=5)
    response.raise_for_status()
except requests.exceptions.ConnectionError:
    print("Could not connect to the API")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError:
    print(" API returned an HTTP error")
print("Program continues")

