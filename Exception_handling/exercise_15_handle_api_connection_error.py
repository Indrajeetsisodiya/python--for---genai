'''
Exercise 15: Handle an AI API connection error

Problem:
Your GenAI application uses a function called:

call_ai_api()

The function may raise a ConnectionError when the AI
service cannot be reached.

The function is provided below:

def call_ai_api():
    raise ConnectionError("AI API is unreachable.")

Your task:

1. Call call_ai_api() inside a try block.
2. Store the returned value in a variable called response.
3. Catch ConnectionError using "as error".
4. Print:

API connection failed: <actual error>

5. If the API call succeeds, use else to print:

API response received: <response>

6. Always use finally to print:

API request finished.

Do NOT modify the call_ai_api() function.

# solution
'''

def call_ai_api():
    raise ConnectionError("AI API is unreachable.")

# solution
try:
    response = call_ai_api ()
except ConnectionError as error:
    print(f"API connection failed:{error}")
else:
    print(f"API response received:{response}")
finally:
    print("API request finished.")

