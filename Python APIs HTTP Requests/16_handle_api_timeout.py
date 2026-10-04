# Exercise 16 — Handle an API Timeout

# Use this URL:
# https://httpbin.org/delay/10

# This endpoint intentionally waits 10 seconds before responding.

# Tasks:
# 1. Send a GET request to the URL.
# 2. Set the timeout to 2 seconds.
# 3. Use try/except to catch:
#    requests.exceptions.Timeout
# 4. If a timeout occurs, print:
#    Request timed out
# 5. After the try/except block, print:
#    Program continues

# Expected output:
# Request timed out
# Program continues

# solution
import requests 
try:
    response = requests.get("https://httpbin.org/delay/10", timeout= 2)
except requests.exceptions.Timeout:
    print("Request timed out ")
print("program continues")

