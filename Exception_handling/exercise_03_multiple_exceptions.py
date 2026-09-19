'''
Exercise 3: Handle multiple possible exceptions

Problem:
Your AI application calculates how many documents can be
processed based on a processing limit.

The user enters a number.

The program performs:

documents = 100 / number

Two different problems can occur:

1. The user enters something that isn't a number.
   Example: "ten"

2. The user enters 0.
   Dividing by zero causes a ZeroDivisionError.

Your task:

1. Put the risky code inside a try block.
2. Create one except block for ValueError.
3. Create another except block for ZeroDivisionError.
4. Print these messages:

For invalid input:
Please enter a valid number.

For zero:
The processing limit cannot be zero.

5. If everything succeeds, use else to print:

Documents that can be processed: <result>

# solution
'''

user_input = input("Enter the processing limit: ")

try:
    number = int(user_input)
    documents = 100 / number
except ValueError:
    print("please enter a valid number ")
except ZeroDivisionError:
    print("the processing limit can not be zero")

else:
    print(f"documents that can be processed are :",int(documents))