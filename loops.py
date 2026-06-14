# Exercise 1: Print each message with its number, starting from 1.
messages = ["Hello", "How are you?", "Tell me about Python", "What is AI?"]
for index, message in enumerate(messages, start=1):
    print(index, message)

# Exercise 2: Count how many messages are in the list without using len().
messages = ["Hello", "How are you?", "Tell me about Python", "What is AI?", "Thanks"]
message_count = 0
for message in messages:
    message_count += 1
print(f"Total messages: {message_count}")

# Exercise 3: Count the number of non-empty prompts.
prompts = ["Write a poem", "", "Explain Python loops", "", "Summarize this article"]
valid_prompt_count = 0
for prompt in prompts:
    if prompt != "":
        valid_prompt_count += 1
print(f"Non-empty prompts: {valid_prompt_count}")

# Exercise 4: Count the total number of characters across all messages.
messages = ["Hello", "AI is amazing", "Python", "ChatGPT", "Thanks"]
character_count = 0
for message in messages:
    for character in message:
        character_count += 1
print(f"Total characters: {character_count}")

# Exercise 5: Find the longest response without using max().
responses = ["AI", "Python", "Machine Learning", "GPT"]
longest_response = ""
for response in responses:
    if len(response) > len(longest_response):
        longest_response = response
print(f"Longest response: {longest_response}")

# Exercise 6: Count how many log entries contain the word 'ERROR'.
logs = [
    "INFO: Model loaded",
    "ERROR: API key missing",
    "INFO: Request received",
    "ERROR: Rate limit exceeded",
    "INFO: Response sent"
]
error_count = 0
for log in logs:
    if "ERROR" in log:
        error_count += 1
print(f"Total errors: {error_count}")

# Exercise 7: Combine all prompts into one string separated by " | ".
prompts = ["Write a poem", "Explain AI", "Python loops", "Machine Learning"]
combined_prompts = ""
for index, prompt in enumerate(prompts):
    combined_prompts += prompt
    if index != len(prompts) - 1:
        combined_prompts += " | "
print(combined_prompts)

# Exercise 8: Count the total number of words across all responses.
responses = ["Python is easy", "AI is powerful", "Loops are useful"]
word_count = 0
for response in responses:
    words = response.split()
    for word in words:
        word_count += 1
print(f"Total words: {word_count}")

# Exercise 9: Create a new list containing only non-empty prompts.
prompts = ["Write a poem", "", "Explain Python", "", "Tell me about AI"]
valid_prompts = []
for prompt in prompts:
    if prompt != "":
        valid_prompts.append(prompt)
print(valid_prompts)

# Exercise 10: Convert all messages to uppercase and store them in a new list.
messages = ["hello", "python", "ai", "chatgpt"]
uppercase_messages = []
for message in messages:
    uppercase_messages.append(message.upper())
print(uppercase_messages)

# Exercise 11: Create a new list containing only messages whose length is greater than 3.
messages = ["Hello", "AI", "Python", "GPT", "Machine Learning"]
long_messages = []
for message in messages:
    if len(message) > 3:
        long_messages.append(message)
print(long_messages)

# Exercise 12: Find the highest score without using max().
scores = [78, 92, 65, 88, 95, 70]
highest_score = scores[0]
for score in scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

# Exercise 13: Find the lowest score without using min().
scores = [78, 92, 65, 88, 95, 70]
lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score
print(lowest_score)

# Exercise 14: Create a new list containing the length of each prompt
prompts = [
    "Write a poem",
    "Explain AI",
    "Python loops",
    "Machine Learning"
]

new_list = []

for prompt in prompts:
    new_list.append(len(prompt))

print(new_list)

# Exercise 15: Create a new list that contains the lengths of only the non-empty prompts.
prompts = [
    "Write a poem",
    "",
    "Explain AI",
    "Python loops",
    "",
    "Machine Learning"
]

new_list = []

for prompt in prompts:
    if prompt != "":
        new_list.append(len(prompt))

print(new_list)
