"""
Introduction to Strings in Python
---------------------------------
This file provides a clear explanation of Python strings,
their types, usage, and multiple example programs.
"""

# -----------------------------
# 1. INTRODUCTION TO STRINGS
# -----------------------------
# A string is a sequence of characters enclosed in single quotes (' '),
# double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable in Python — once created, they cannot be changed.

single_q = 'Hello World'
double_q = "Hello Python"
triple_q = """This is a
multiline string"""

print("Single Quote:", single_q)
print("Double Quote:", double_q)
print("Triple Quote:", triple_q)

# -----------------------------
# 2. TYPES OF STRINGS
# -----------------------------
#  - Single-line strings
#  - Multi-line strings
#  - Raw strings (ignore escape sequences)
#  - Unicode strings

single_line = "Python is easy"
multi_line = """Python
String
Example"""
raw_string = r"C:\\Users\\Subham\\Folder"

print(single_line)
print(multi_line)
print(raw_string)

# -----------------------------
# 3. STRING USAGE
# -----------------------------
# Strings are commonly used for:
#   - Taking input
#   - Displaying output
#   - Storing text data
#   - File handling
#   - Data processing

# Example: Taking user input (commented to avoid interruption)
# name = input("Enter your name: ")
# print("Hello", name)

# -----------------------------
# 4. STRING OPERATIONS
# -----------------------------
# Concatenation (+)
# Repetition (*)
# Indexing
# Slicing
# Length

s1 = "Hello"
s2 = "Python"
print(s1 + " " + s2)          # concatenation
print(s1 * 3)                  # repetition
print(s1[1])                   # indexing
print(s2[1:5])                 # slicing
print(len(s1))                 # length

# -----------------------------
# 5. STRING METHODS
# -----------------------------
text = "python programming"

print(text.upper())
print(text.capitalize())
print(text.title())
print(text.replace("python", "java"))
print(text.split())
print(text.find("prog"))

# -----------------------------
# 6. IMPLEMENTATION EXAMPLES
# -----------------------------

# Program 1: Count vowels in a string
string = "Hello Python World"
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print("Total vowels:", count)

# Program 2: Reverse a string
text = "Python"
print("Reversed:", text[::-1])

# Program 3: Palindrome check
word = "madam"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is NOT a palindrome")

# Program 4: Count occurrences of each character
sentence = "banana"
char_count = {}
for char in sentence:
    char_count[char] = char_count.get(char, 0) + 1
print("Character frequency:", char_count)

# Program 5: Remove spaces from a string
line = "Python is fun"
no_space = line.replace(" ", "")
print(no_space)
