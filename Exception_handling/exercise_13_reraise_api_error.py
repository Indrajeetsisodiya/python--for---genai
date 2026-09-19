'''
Exercise 13: Re-raise an API-style error

Problem:
Imagine an AI API function that receives a response.

The response should contain an "answer" key.

Sometimes the key is missing.

Your task:

1. Create this dictionary:

response = {
    "status": "success"
}

2. Create a try block that attempts to get:

answer = response["answer"]

3. Catch the KeyError using "as error".

4. Inside the except block:
   - Print:

API response error: <actual error>

   - Then use "raise" to re-raise the same exception.

5. Outside the first try/except, create another try/except
   that calls the code above and catches the KeyError.

6. The outer except should print:

The application handled the API error.

Important:
The purpose of this exercise is to understand that
an exception can be caught, processed, and then passed
to a higher level using "raise".

# solution
'''
response = {
    "status": "success"
}

try:

    try:
        answer = response["answer"]

    except KeyError as error:
        print(f"API response error:{error}")
        raise
except KeyError:
    print("The application handled the API error.")




