'''
Exercise 7: Access Data from a Nested Dictionary

Problem:
You receive an API-like user response:

user = {
    "id": 101,
    "profile": {
        "name": "Alex",
        "language": "English",
        "experience": "beginner"
    }
}

Print:

1. The user's name
2. The user's language

Expected Output:
Alex
English
'''

# solution
user = {
    "id": 101,
    "profile": {
        "name": "Alex",
        "language": "English",
        "experience": "beginner"
    }
}

print(user["profile"]["name"])
print(user["profile"]["language"])