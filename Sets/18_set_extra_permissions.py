'''
Exercise 18: Find Extra Permissions

Problem:
An AI application requires these permissions:

required_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

A user has these permissions:

user_permissions = {
    "read_documents",
    "search_documents",
    "generate_response",
    "upload_documents",
    "delete_documents"
}

Find the permissions the user has that are NOT required
by the application.

Store the result in `extra_permissions`.

Print `extra_permissions`.

Expected output:
{'upload_documents', 'delete_documents'}

Hint:
Think about the set operation that finds items in the
first set but NOT in the second set.
'''

# solution
required_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

user_permissions = {
    "read_documents",
    "search_documents",
    "generate_response",
    "upload_documents",
    "delete_documents"
}

extra_permissions = user_permissions.difference(required_permissions)
print(extra_permissions)

