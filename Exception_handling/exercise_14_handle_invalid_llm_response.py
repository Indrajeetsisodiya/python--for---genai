'''
Exercise 14: Handle an invalid LLM response

Problem:
Your GenAI application expects an LLM response to be a string.

The application wants to convert the response to lowercase
before further processing.

Use this response:

response = None

Your task:

1. Try to call .lower() on the response.
2. Store the result in a variable called cleaned_response.
3. Catch the appropriate exception.
4. If the exception occurs, print:

Invalid LLM response.

5. If the operation succeeds, use else to print:

Cleaned response: <cleaned_response>

6. Always use finally to print:

LLM response processing finished.

Test your code first with:

response = None

Then change it to:

response = "The Answer Is Paris"

and test it again.

Hint:
Calling a method that an object doesn't have causes AttributeError.

# solution
'''
response = None
try:
    cleaned_response = response.lower()
except AttributeError:
    print("Invalid LLM response.")
else:
    print(f"Cleaned response:{cleaned_response}")
finally:
    print("LLM response processing finished.")
    


