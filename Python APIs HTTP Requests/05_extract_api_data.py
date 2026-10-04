
# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Send a GET request to the API.
# 2. Convert the response into Python data using .json().
# 3. Store the result in a variable called `data`.
# 4. Print only the `title` from the API response.

# solution
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()
print(data["title"])

# output = sunt aut facere repellat provident occaecati excepturi optio reprehenderit