'''
Exercise 4: Remove Unwanted API Data

Problem:
You receive the following API-like response:

api_response = {
    "user_id": 101,
    "name": "Alex",
    "email": "alex@example.com",
    "password": "secret123",
    "role": "user"
}

Your application does not need the "password" field.

Remove the "password" key from the dictionary.

Then print the entire dictionary.

Expected Output:
{
    "user_id": 101,
    "name": "Alex",
    "email": "alex@example.com",
    "role": "user"
}
'''

# solution
api_response = {
    "user_id": 101,
    "name": "Alex",
    "email": "alex@example.com",
    "password": "secret123",
    "role": "user"
}

api_response.pop("password")
print(api_response)
