# Exercise 9 — Multiple Query Parameters

# Use this API:
# https://jsonplaceholder.typicode.com/posts

# Tasks:
# 1. Create a `params` dictionary with:
#    userId = 1
#    id = 3
# 2. Send a GET request using the `params` argument.
# 3. Store the response in `response`.
# 4. Convert the response using `.json()`.
# 5. Store the resuld

# The API should return the post matching both conditions.

# solution
import requests
params = {"userId":1 , "id" : 3}
response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params)
data = response.json()
print(data)
