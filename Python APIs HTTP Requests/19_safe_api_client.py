# Exercise 19 — Build a Safe API Client

# Use this API:
# https://jsonplaceholder.typicode.com/posts/999999

# Tasks:
# 1. Create a function called `safe_get_api_data`.
# 2. The function should accept a `url` parameter.
# 3. Inside the function, use try/except.
# 4. Send a GET request with a timeout of 5 seconds.
# 5. Call raise_for_status().
# 6. Convert a successful response to Python data using .json().
# 7. Return the data if the request succeeds.
# 8. Catch ConnectionError and print:
#    Could not connect to the API
# 9. Catch Timeout and print:
#    Request timed out
# 10. Catch HTTPError and print:
#     API returned an HTTP error
# 11. If any of these errors occur, return None.
# 12. Call the function using the API URL above.
# 13. Store the result in a variable called `data`.
# 14. Print `data`.

# solution
import requests

def safe_get_api_data(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        python_data = response.json()
        return python_data
    except requests.exceptions.ConnectionError:
        print("Could not connect to the API")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError:
        print("API returned an HTTP error")
    return None

data = safe_get_api_data("https://jsonplaceholder.typicode.com/posts/999999")
print(data)

if data is None:
    print("No data received")
