'''
Exercise 10: Find Missing Permissions

Problem:
An AI application requires these permissions to use all of its features:

required_permissions = {
    "read_documents",
    "search_documents",
    "generate_response",
    "upload_documents"
}

A user currently has:

user_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

Find which required permissions the user is missing.

Store the missing permissions in a variable called `missing_permissions`.

Print `missing_permissions`.

Expected output:
{'upload_documents'}

Hint:
Think about the set operation that finds items
present in one set but not another.
'''

# solution
required_permissions = {
    "read_documents",
    "search_documents",
    "generate_response",
    "upload_documents"
}

user_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

missing_persmissions = required_permissions.difference(user_permissions)
print(missing_persmissions)

