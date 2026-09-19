'''
Exercise 16: Handle multiple AI API failures

Problem:
Simulate an AI API request that can have three outcomes.

Ask the user to enter one of these:

connection
timeout
success

Your program should behave as follows:

If the user enters "connection":
Raise a ConnectionError with the message:

"AI API could not be reached."

If the user enters "timeout":
Raise a TimeoutError with the message:

"AI API took too long to respond."

If the user enters "success":
Return:

"The AI response was successful."

Your task:

1. Create a function called call_ai_api().
2. The function should receive the user's choice.
3. Inside the function, handle the three possible choices
   described above.
4. Call the function from your main code.
5. Handle ConnectionError separately.
6. Handle TimeoutError separately.
7. Use "as error" in both except blocks.
8. For a connection error, print:

Connection problem: <error>

9. For a timeout, print:

API timeout: <error>

10. If successful, use else to print:

AI response: <response>

11. Always use finally to print:

AI request completed.

Test all three inputs:

connection
timeout
success

# solution
'''
def call_ai_api(user_input):
    if user_input == "connection":
        raise ConnectionError("AI API could not be reached.")
    elif user_input == "timeout":
        raise TimeoutError("AI API took too long to respond.")
    elif user_input == "success":
        return "The AI response was successful."

user_input = input("enter the input: ")


try:
    response = call_ai_api(user_input)
except ConnectionError as error:
    print(f"Connection problem:{error}")
except TimeoutError as error:
    print(f"API timeout:{error}")
else:
    print(f"AI response:{response}")
finally:
    print("AI request completed.")
    









