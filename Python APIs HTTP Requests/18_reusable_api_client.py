# Exercise 18 — Build a Reusable API Client Function

# Use this API:
# https://jsonplaceholder.typicode.com/posts/1

# Tasks:
# 1. Create a function called `get_api_data`.
# 2. The function should accept a `url` parameter.
# 3. Inside the function:
#    - Send a GET request to the URL.
#    - Check the response using raise_for_status().
#    - Convert the response to Python data using .json().
#    - Return the data.
# 4. Call your function using the API URL above.
# 5. Store the returned data in a variable called `data`.
# 6. Print `data`.

# solution

import requests
def get_api_data(url):
    response = requests.get(url)
    response.raise_for_status()
    python_data = response.json()
    return python_data

data = get_api_data("https://jsonplaceholder.typicode.com/posts/1")
print(data)


