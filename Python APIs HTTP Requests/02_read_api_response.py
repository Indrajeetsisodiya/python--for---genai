# Exercise 2 — Read the API Response

# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Import the requests library.
# 2. Send a GET request to the API.
# 3. Store the response in a variable called `response`.
# 4. Convert the response into Python data using .json().
# 5. Store the converted data in a variable called `data`.
# 6. Print the data.

# Expected output:
# A Python dictionary containing userId, id, title, and body.

# solution

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()

print(data)

# output = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
