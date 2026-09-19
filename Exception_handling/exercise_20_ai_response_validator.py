'''
You are processing a response from an AI API.

Ask the user to enter a JSON response.

The response should contain:
- "answer"
- "confidence"

Your program must:

1. Convert the user's JSON text into a Python dictionary.

2. Get "answer" using dict.get().
   If it is missing, use "No answer provided".

3. Get "confidence" using dict.get().
   If it is missing, use 0.

4. Check the confidence value:
   - If confidence is less than 0 or greater than 1,
     manually raise a ValueError with the message:
     "Confidence must be between 0 and 1."

5. Handle these errors separately:
   - JSONDecodeError → print "Invalid JSON:" followed by the error.
   - ValueError → print "Invalid confidence:" followed by the error.

6. If everything is successful, use else to print:
   "AI response is valid."

7. Use finally to print:
   "AI response processing finished."

Test your program with:

Test 1:
{"answer": "Paris", "confidence": 0.95}

Test 2:
{"answer": "Paris", "confidence": 1.5}

Test 3:
{"answer": "Paris"

Test 4:
{"confidence": 0.8}
'''

# solution
import json
user_input = input("enter json document: ")

try:
    data = json.loads(user_input)
    print(data.get("answer","No answer provided"))
    print(data.get("confidence",0))
    if data.get("confidence") < 0 or data.get("confidence") > 1:
        raise ValueError("Confidence must be between 0 and 1.")
except json.JSONDecodeError as error:
    print(f"Ivalid JSON:",error)
except ValueError as error:
    print("Invalid confidence:",error)
else:
    print("AI response is valid.")
finally:
    print("AI response processing finished.")

'''
test results-
first test = 
Paris
0.95
AI response is valid.
AI response processing finished.

second test = 
Paris
1.5
Invalid confidence: Confidence must be between 0 and 1.
AI response processing finished.

third test = 
enter json document: {"answer": "Paris"
Ivalid JSON: Expecting ',' delimiter: line 1 column 19 (char 18)
AI response processing finished.

fourth test = 
No answer provided
0.8
AI response is valid.
AI response processing finished.

'''
