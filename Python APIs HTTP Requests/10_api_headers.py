# Exercise 10 — Send an HTTP Header

# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Create a dictionary called `headers`.
# 2. Add this header:
#    "Content-Type": "application/json"
# 3. Send a GET request to the API using the `headers` argument.
# 4. Store the response in `response`.
# 5. Print the status code.

# Expected output:
# 200

# solution
import requests
header = {"Content-Type": "application/json"}
response = requests.get("https://jsonplaceholder.typicode.com/posts/1",headers=header)
print(response.status_code)

# output = 200