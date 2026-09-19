'''
Exercise 1: Handle invalid user input

Problem:
You are building a small AI application that asks the user
to enter the maximum number of documents they want to process.

The user should enter a number.

The starter code below works when the user enters a valid integer,
but crashes when the user enters something like:

"five"
"10 documents"
"abc"

Your task:

1. Put the code that can cause the error inside a try block.
2. Catch the appropriate exception.
3. If the user enters a valid number, print:

Documents to process: <number>

4. If the user enters invalid input, print:

Please enter a valid number.

Example:

Input:
5

Output:
Documents to process: 5

Example:

Input:
five

Output:
Please enter a valid number.

Hint:
The error caused by converting invalid text into an integer
is ValueError.

Use try and except.

# solution
'''

user_input = input("How many documents should the AI process? ")

try:
    number = int(user_input)
except ValueError:
    print("enter the valid number !")
else:
    print("Documents to process:", number)



    




