# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Send a GET request to the API.
# 2. Print the raw response using response.text.
# 3. Convert the response using response.json().
# 4. Print the converted Python data.
# 5. Observe the difference between the two outputs.

# solution
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.text)
data = response.json()
print(data)

