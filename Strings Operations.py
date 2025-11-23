"""
Python Strings Operations: Explanation, Illustration, Usage, Examples & Programs
-------------------------------------------------------------------------------
This file contains detailed explanations of string operations in Python along with
illustrations, examples, and programs for easy understanding.
"""

# =============================
# 1. INTRODUCTION TO STRINGS
# =============================
# A string is a sequence of characters. It is immutable and can be created using:
#   - Single quotes (' ')
#   - Double quotes (" ")
#   - Triple quotes for multi-line strings (''' ''' or """ """)

s1 = 'Hello'
s2 = "Python"
s3 = """This is a 
multiline string"""

print(s1)
print(s2)
print(s3)

# =============================
# 2. STRING OPERATIONS (with explanation & illustration)
# =============================

# -----------------------------------------------------
# A. CONCATENATION (+)
# -----------------------------------------------------
# Joins two or more strings.
fname = "Subham"
lname = "Kumar"
full_name = fname + " " + lname
print("Concatenation:", full_name)

# -----------------------------------------------------
# B. REPETITION (*)
# -----------------------------------------------------
# Repeats a string multiple times.
print("Repeat:", "Hi" * 3)

# -----------------------------------------------------
# C. INDEXING (Access characters)
# -----------------------------------------------------
# Positions start from 0.
name = "PYTHON"
print(name[0])   # P
print(name[3])   # H
print(name[-1])  # last character

# -----------------------------------------------------
# D. SLICING (Extract substring)
# -----------------------------------------------------
# Syntax: string[start: end: step]
text = "Programming"
print(text[0:6])      # Progra
print(text[3:])       # gram...
print(text[:5])       # Progr
print(text[::-1])     # reverse

# -----------------------------------------------------
# E. LENGTH (len())
# -----------------------------------------------------
print("Length:", len(text))

# -----------------------------------------------------
# F. MEMBERSHIP (in, not in)
# -----------------------------------------------------
print("Pro" in text)
print("xyz" not in text)

# -----------------------------------------------------
# G. ITERATION (loop through string)
# -----------------------------------------------------
for ch in "ABC":
    print(ch)

# =============================
# 3. STRING METHODS
# =============================

msg = "python string operations"
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())
print(msg.replace("python", "java"))
print(msg.split())
print(msg.find("string"))
print(msg.count("t"))
print(msg.startswith("python"))
print(msg.endswith("ions"))

# strip methods
sample = "   hello world   "
print(sample.strip())
print(sample.lstrip())
print(sample.rstrip())

# =============================
# 4. STRING FORMATTING
# =============================

# Using format()
print("My name is {} and I am {} years old".format("Subham", 20))

# Using f-strings
age = 20
print(f"My name is Subham and I am {age} years old")

# =============================
# 5. STRING PROGRAMS (Practical Examples)
# =============================

# Program 1: Count vowels in a string
s = "Hello Python"
vowels = "aeiouAEIOU"
c = 0
for ch in s:
    if ch in vowels:
        c += 1
print("Vowel count =", c)

# Program 2: Reverse a string
st = "Python"
print("Reverse:", st[::-1])

# Program 3: Palindrome check
word = "madam"
if word == word[::-1]:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")

# Program 4: Count character frequency
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("Frequency:", freq)

# Program 5: Remove spaces
line = "Python is fun"
print(line.replace(" ", ""))

# Program 6: Find longest word in a sentence
sentence = "Python makes programming easy and powerful"
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)

# Program 7: Convert string to list without split
s = "Hello"
print(list(s))

# Program 8: Print characters with their ASCII values
for ch in "ABC":
    print(ch, ord(ch))

# Program 9: Swap case manually
s = "PyThOn"
result = ""
for ch in s:
    if ch.islower():
        result += ch.upper()
    else:
        result += ch.lower()
print(result)

# Program 10: Check if string contains only alphabets
string = "Python123"
if string.isalpha():
    print("Alphabet only")
else:
    print("Contains non-alphabets")
