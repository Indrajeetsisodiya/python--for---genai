'''
Exercise 11: Handle different file access errors

Problem:
Your document-processing application asks the user
for a filename and tries to open it for reading.

Two different problems can occur:

1. The file does not exist.
   → FileNotFoundError

2. The file exists but Python does not have permission
   to read it.
   → PermissionError

Your task:

1. Ask the user for a filename.
2. Try to open the file in read mode.
3. Handle FileNotFoundError separately.
4. Handle PermissionError separately.
5. Print:

If the file doesn't exist:
Document not found.

If permission is denied:
Permission denied.

6. If the file opens successfully, use else to print:

Document opened successfully.

7. Always use finally to print:

Document access attempt finished.

# solution
'''
user_input = input("enter document name : ")

try:
    file = open(user_input , "r")
except FileNotFoundError:
    print("document not found")
except PermissionError:
    print("Permission is denied")
else:
    print("document opened successfully")
finally:
    print("document attempt finished successfully")