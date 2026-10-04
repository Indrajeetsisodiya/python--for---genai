# Use this API:
# https://httpbin.org/post
#
# This API does not generate a real AI response.
# It simply sends your JSON data back to you.
# We will use it to simulate an LLM-style API workflow.
#
# Tasks:
#
# 1. Ask the user to enter a prompt.
#
# 2. Create a dictionary containing:
#    - "model": "demo-llm"
#    - "prompt": the user's input
#
# 3. Send the dictionary to https://httpbin.org/post
#    using a POST request and JSON data.
#
# 4. Set a timeout of 5 seconds.
#
# 5. Use raise_for_status() to detect HTTP errors.
#
# 6. Convert the JSON response into Python data.
#
# 7. Extract and print the prompt that was sent.
#    Hint: the response contains the JSON you originally sent
#    inside a "json" key.
#
# 8. Handle these errors separately:
#    - ConnectionError
#    - Timeout
#    - HTTPError
#
# 9. If an error occurs, print an appropriate message
#    and make the function return None.
#
# 10. Put the API call inside a reusable function:
#     call_ai_api(prompt)
#
# 11. Call the function with the user's prompt and print
#     the returned result.
#
# Goal:
# Combine what you have learned about:
# requests
# GET/POST
# JSON
# status codes
# raise_for_status()
# timeout
# exceptions
# functions
# API request/response flow
#
# Do not use OpenAI or any real AI provider API.
#
# solution
import requests
user_input = input("enter prompt : ")
def call_ai_api(prompt):
    try:
        my_dict = {
            "model": "demo-llm",
            "prompt": prompt
        }
        response = requests.post("https://httpbin.org/post", json=my_dict , timeout=5)
        response.raise_for_status()
        python_data = response.json()
        return python_data["json"]["prompt"]
   
    except requests.exceptions.ConnectionError:
        print("couldn't connect to the api")
    except requests.exceptions.Timeout:
        print("request timed out")
    except requests.exceptions.HTTPError:
        print("API returned HTTP error")
    return None

data = call_ai_api(user_input)
print(data)

if data is None:
    print("No data received")








