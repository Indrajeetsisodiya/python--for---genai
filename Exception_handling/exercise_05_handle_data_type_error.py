'''
Exercise 5: Handle invalid data types

Problem:
Your AI application receives document information.

Sometimes the word count is correctly stored as an integer.
Sometimes bad data enters the system.

Use these two test cases separately:

Test 1:
word_count = 5000

Test 2:
word_count = "5000"

Your task:

1. Calculate the processing cost using:

cost = word_count * 0.01

2. Handle any appropriate exception that can occur.
3. If the calculation succeeds, use else to print:

Estimated processing cost: <cost>

4. Use finally to print:

Cost calculation finished.

Important:
Think carefully about what happens when word_count is a string.

# solution
'''
# Test 1
word_count = 5000

try:
    cost = word_count * 0.01
except TypeError:
    print("type error occured")
else:
    print(cost)

# Test 2
word_count = "5000"
try:
    cost = word_count * 0.01
except TypeError:
    print("type error occured")
else:
    print(cost)

finally:
    print("Cost calculation finished.")