'''
Exercise 9: Check User Permissions

Problem:
An AI application has these available permissions:

available_permissions = {
    "read_documents",
    "upload_documents",
    "search_documents",
    "generate_response",
    "delete_documents"
}

A user has these permissions:

user_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

Your application wants to allow the user to perform these actions:

required_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

Check whether the user has ALL the required permissions.

Store the result in a variable called `has_access`.

Print `has_access`.

Expected output:
True

Hint:
Think about comparing sets rather than checking each permission
individually.
'''

# solution
user_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

required_permissions = {
    "read_documents",
    "search_documents",
    "generate_response"
}

has_access = user_permissions.issubset(required_permissions) #issubset() method used here 
print(has_access)


