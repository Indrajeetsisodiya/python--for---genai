# Exercise 11 — Your First POST Request

# Use this API:
# https://jsonplaceholder.typicode.com/posts

# Tasks:
# 1. Create a Python dictionary called `data`.
# 2. Add these key-value pairs:
#    "title": "Learning APIs"
#    "body": "I am learning Python APIs for GenAI development."
#    "userId": 1
# 3. Send a POST request to the API.
# 4. Send `data` as JSON using the `json=` argument.
# 5. Store the response in `response`.
# 6. Print the response status code.
# 7. Print the response JSON.

# Expected status code:
# 201

# solution
import requests
data = {
    "title" : "learning APIs" ,
    "body"  : "I am learning python APIs for GenAI development.",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
print(response.status_code)
print(response.json())

