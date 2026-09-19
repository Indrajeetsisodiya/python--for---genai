'''
Exercise 6: Handle errors in an API-style response

Problem:
Your AI application receives this response:

response = {
    "status": "success",
    "tokens": "250"
}

You need to read the number of tokens and convert it
into an integer.

Two things can go wrong:

1. The "tokens" key might be missing.
   → KeyError

2. The "tokens" value might contain invalid data.
   Example:
   "tokens": "two hundred"
   → ValueError

Your task:

1. Try to access the "tokens" value and convert it to an integer.
2. Handle KeyError separately.
3. Handle ValueError separately.
4. If successful, use else to print:

Tokens used: <number>

5. Use finally to print:

Token processing finished.

Test your code with these three responses:

Response 1:
{
    "status": "success",
    "tokens": "250"
}

Response 2:
{
    "status": "success"
}

Response 3:
{
    "status": "success",
    "tokens": "two hundred"
}

# solution
'''

response = {
    "status": "success",
    "tokens": "250"
}
try:
    response["tokens"] = int(response["tokens"])
except KeyError:
    print("keyerror has occured")
except ValueError:
    print("value error has occured")
else:
    print(response["tokens"])
finally:
    print("Token processing finished.")


response = {
    "status": "success"
}
try:
    response["tokens"] = int(response["tokens"])
except KeyError:
    print("keyerror has occured")
except ValueError:
    print("value error has occured")
else:
    print(response["tokens"])
finally:
    print("Token processing finished.")

response = {
    "status": "success",
    "tokens": "two hundred"
}
try:
    response["tokens"] = int(response["tokens"])
except KeyError:
    print("keyerror has occured")
except ValueError:
    print("value error has occured")
else:
    print(response["tokens"])
finally:
    print("Token processing finished.")



