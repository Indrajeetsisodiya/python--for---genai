'''
Exercise 18: Handle invalid JSON from an AI API

Problem:
Your GenAI application receives JSON data as a string.

Sometimes the API returns malformed JSON.

Use the json module to convert the JSON string into
a Python dictionary.

Test with:

'{"answer": "Paris", "confidence": 0.95}'

and then test with:

'{"answer": "Paris", "confidence": 0.95'

Your task:

1. Import the json module.
2. Ask the user to enter the JSON response.
3. Try to convert the JSON string into a Python dictionary.
4. Catch JSONDecodeError.
5. Use "as error" and print:

Invalid JSON response: <error>

6. If parsing succeeds, use else to print:

JSON parsed successfully.

7. Always use finally to print:

JSON processing finished.

# solution
'''
import json

user_input = input("Please enter JSON response: ") #{"answer": "Paris", "confidence": 0.95} enter this 
try:
    data = json.loads(user_input) #json.loads() takes a JSON-formatted string and converts it into a Python object.
except json.JSONDecodeError as error:
    print(error)
else:
    print("JSON parsed successfully.")
finally:
    print("JSON processing finished.")

