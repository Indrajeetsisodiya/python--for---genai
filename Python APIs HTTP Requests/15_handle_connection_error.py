# Exercise 15 — Handle a Connection Error

# Use this intentionally invalid URL:
# https://this-api-does-not-exist-12345.com

# Tasks:
# 1. Send a GET request to the URL.
# 2. Use try/except to catch:
#    requests.exceptions.ConnectionError
# 3. If a ConnectionError occurs, print:
#    Could not connect to the API
# 4. After the try/except block, print:
#    Program continues

# Expected output:
# Could not connect to the API
# Program continues

# solution
import requests
try:
    response = requests.get("https://this-api-does-not-exist-12345.com")
except requests.exceptions.ConnectionError:
    print("Could not connect to the API")
print("Program continues")
