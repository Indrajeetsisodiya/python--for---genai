'''
You received a response from an AI API.

Ask the user to enter a JSON response.

Your program must:

1. Convert the user's JSON text into a Python dictionary.
2. Handle invalid JSON using JSONDecodeError.
3. Safely retrieve "answer" using dict.get().
4. Safely retrieve "confidence" using dict.get().
5. If "answer" is missing, use "No answer provided" as the default.
6. If "confidence" is missing, use 0 as the default.
7. Print both values.
8. Use else to print:
   "Response processed successfully."
9. Use finally to print:
   "Response processing finished."

Test your program with:

Valid JSON:
{"answer": "Paris", "confidence": 0.95} 

Missing keys:
{"answer": "Paris"}

Invalid JSON:
{"answer": "Paris"
'''

# solution
import json

user_input = input("enter json document: ") #{"answer": "Paris", "confidence": 0.95} enter this 

try:
   data = json.loads(user_input)
   print(data.get("answer","no answer provided"))
   print(data.get("confidence",0))

except json.JSONDecodeError as error:
    print(error)
else:
   print("Response processed successfully.")
finally:
    print("Response processing finished.")


'''
Test results :

Valid JSON:
{"answer": "Paris", "confidence": 0.95} 
result =
Response processed successfully.
Response processing finished.
Paris
0.95

Missing keys:
{"answer": "Paris"}
result = 
Response processed successfully.
Response processing finished.
Paris
0

Invalid JSON:
{"answer": "Paris"
result = 
Expecting ',' delimiter: line 1 column 19 (char 18)
Response processing finished.

'''


