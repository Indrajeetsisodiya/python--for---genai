# Exercise 8 — Use Query Parameters

# Use this API:
# https://jsonplaceholder.typicode.com/posts

# Tasks:
# 1. Import the requests library.
# 2. Create a variable called `params`.
# 3. Store this dictionary in it:
#    {"userId": 1}
# 4. Send a GET request to the API using the `params` argument.
# 5. Store the response in a variable called `response`.
# 6. Convert the response to Python data using `.json()`.
# 7. Print the resulting data.

# The API should return posts belonging to userId 1.

# solution
import requests
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params)
data = response.json()
print(data)
