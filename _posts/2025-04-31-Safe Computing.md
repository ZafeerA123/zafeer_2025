---
layout: post
title: Safe Computing
description: Notes for Safe computing lesson (4.1.2025)
type: issues 
comments: true
permalink: safe_computing
categories: [Big Idea]
---

# Popcorn Hack 1
  <div id="123456">
    <img src="{{site.baseurl}}/images/cookies.png" style="width: 190000px;">
  </div>
<br><br>

# Popcorn Hack 2
  <div id="123456">
    <img src="{{site.baseurl}}/images/CAPTCHA1.png" style="width: 190000px;">
  </div>
<br><br>

# Homework Hack 1

- Submitted online

# [Homework Hack 2](https://www.programiz.com/online-compiler/5JeIGizm279hJ)

Code: 

```python
import random

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # This part of the code only encrypts letters
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char  # this keeps the spaces and punctuation unchanged
    return result

# Here is the code for getting the user input
mode = input("Do you want to encrypt or decrypt? ").strip().lower()
message = input("Enter your message: ")

# Get the shift value, either a random value or user input
shift_input = input("Enter shift value (number of places to shift) or 'random' for a random shift: ").strip().lower()

# If 'random' is entered, generate a random shift between 1 and 25
if shift_input == 'random':
    shift = random.randint(1, 25)
    print(f"Random shift value chosen: {shift}")
else:
    shift = int(shift_input)

# Finally, perform the encryption or decryption
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
```