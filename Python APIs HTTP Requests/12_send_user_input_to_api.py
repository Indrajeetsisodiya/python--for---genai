# Exercise 12 — Send User Input to an API

# Use this API:
# https://jsonplaceholder.typicode.com/posts

# Imagine the user is entering a message that will eventually
# be sent to an AI service.

# Tasks:
# 1. Ask the user to enter a message using input().
# 2. Store the user's message in a variable called `message`.
# 3. Create a dictionary called `data`.
# 4. Store the user's message under the key `"body"`.
# 5. Add `"title": "User Message"`.
# 6. Add `"userId": 1`.
# 7. Send the dictionary to the API using a POST request and `json=`.
# 8. Store the response in `response`.
# 9. Print the response status code.
# 10. Print the response JSON.

# solution
import requests
message = input("enter message: ")
data = {"body": message , "title": "User Message", "userId": 1}
response  = requests.post("https://jsonplaceholder.typicode.com/posts",json= data)
print(response.status_code)
print(response.json())
