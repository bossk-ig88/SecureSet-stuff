#!/usr/bin/python3
# SYS 200 - 02 LAB - Input Validation
# Check for alphabets, numbers, at least 1 special character.

# import getpass and punctuation
# Prompt the user for a password without echoing
from getpass import getpass

# String of ASCII characters which are considered punctuation characters
# in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
from string import punctuation

blacklist = ["!", "@"]
# Define function for password validator.
def pass_valid(pwd):

    # If input contains a space:
    if ' ' in pwd:
        return "No spaces in password."

    # Over the length of the user's password is not between 20- and 51(50) characters:
    if len(pwd) not in range(2,51):
        return "Password needs 2-50 characters."

    # 1 special character minimum requirement.
    # For the special character in user's password,
    # and if user's special character matches in Punctuation list,
    # the variable is true/valid.
    specials = [True for spec in pwd if spec in punctuation]

    # Blacklist - if user's spec char matches blacklist item:
    if spec != "!":
        pass
    else:
        return f"Invalid. Entry <{spec}> on blacklist. Try again."



    # Over the length of special characters in user input,
    # if no spec character provided:
    if len(specials) == 0:
        return "Acceptable characters (1 req.): ", punctuation

    # 1 number minimum requirement
    # If a number exists in password, this runs true.
    numbers = any(spec.isdigit() for spec in pwd)
    if not numbers:
        return "1 number required."
    # If password parameters solid, “Formatted string literals,”
    # curly braces containing expressions
    # replaced with their values. Prints user's correct password.
    return f"Good password: {pwd}"


# User input.
pwd = getpass("Enter Password: ")


# prints
print(pass_valid(pwd))
