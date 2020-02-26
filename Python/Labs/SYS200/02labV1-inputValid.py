#!/usr/bin/python3
# SYS 200 - 02 LAB - Input Validation
# Check for alphabets, numbers, at least 1 special character.
# Contains no spaces
# Length of password be between 5 and 10 (includsive)
# Have at lesat 1 special characters
# have at least 1 number.

whitelist =


while True:
    try:
        val1 = int(input("Enter the first number: "))
        val2 = int(input("Enter the second number: "))
        break
    except:
        print("You did not enter a number.")
        continue

print(val1/val2)
# Try: Create a password validation program
# that utilizes a white list to only allow specific password characters.
