# Use this API:
# https://httpbin.org/post
#
# Scenario:
# You are building a small AI application.
# A user enters a prompt, and your application sends
# that prompt to an AI-style API.
#
# Tasks:
#
# 1. Ask the user to enter a prompt.
#
# 2. Create a function:
#    send_prompt(prompt)
#
# 3. Inside the function, create this JSON data:
#    {
#        "model": "demo-llm",
#        "prompt": prompt,
#        "temperature": 0.7
#    }
#
# 4. Send the data using POST to the API.
#
# 5. Set timeout=5.
#
# 6. Use raise_for_status().
#
# 7. Convert the response into Python data.
#
# 8. Extract these three values from the API response:
#    - model
#    - prompt
#    - temperature
#
# 9. Return these three values from the function
#    in a dictionary.
#
# 10. Handle:
#     - ConnectionError
#     - Timeout
#     - HTTPError
#
# 11. If an error occurs, return None.
#
# 12. Outside the function:
#     - Call send_prompt() with the user's prompt.
#     - If the result is None, print:
#       "AI request failed"
#     - Otherwise print:
#       "Model: ..."
#       "Prompt: ..."
#       "Temperature: ..."
#
# Important:
# Use the function parameter "prompt" inside the function.
# Do not use the outside variable "user_input" inside the function.
#
# solution
import requests
user_input = input("enter the prompt: ")

def send_prompt(prompt):
    try:
        json_data = {
            "model":"demo-llm",
            "prompt": prompt,
            "temperature": 0.7
            
        }
        response = requests.post("https://httpbin.org/post", json=json_data, timeout=5)
        response.raise_for_status()
        python_data = response.json()
        return python_data["json"]

    except requests.exceptions.ConnectionError:
        print("couldn't establish connection with api")
    except requests.exceptions.Timeout:
        print("request timed out ")
    except requests.exceptions.HTTPError:
        print("API returned http error")
    return None

data = send_prompt(user_input)
if data is None:
    print("No data received")
else:
    print(f"model: {data['model']}")
    print(f"Prompt: {data['prompt']}")
    print(f"temperature: {data['temperature']}")





