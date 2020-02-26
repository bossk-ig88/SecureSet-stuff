# CRY100-1 Lab - Rotation Cipher, encrypt and decrypt, spaces accomodated.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
question = input("'E' for Encrypt, 'D' for Decrypt: ")
result = ""

# User input:
if question == 'E' or question == 'e':
    print("Start ENCRYPTION...")

    # 1. User Input:
    x = input("ENCRYPT: ")

    # 2. User Cipher key shift:
    y = input("Number of Shifts: ")
    # !!!! No need to create a yint variable - just cast to int() later

    # 3. Loop into user input:
    for item in x:

        # ID spaces in user input. Makes decrypting easy (add to result)
        if item.isspace():
            result += item

        # ID alpha characters:
        elif item.isalpha():
            # Calling math function.
            # Calling .upper() function to deal with lower case inputs.
            # (not required later for decryption as decryption is all caps.)
            indexLetter = alphabet.index(item.upper())
            # Cast to int().  Add to result.
            result += alphabet[(indexLetter + int(y)) % 26]

        # Unwanted characters:
        else:
            print("Unwanted Character Found. Replaced with '.'")
            result += '.'

    print("RESULT:",result)

# Decrypt function
elif question == 'D' or question == 'd':
    print("Start DECRYPTION...")

    # 1. User Input:
    x = input("DECRYPT: ")

    # 2. User Cipher key shift:
    y = input("Number of Shifts: ")

    # 3. Loop into user input:
    for item in x:

        # ID spaces in user input. Makes decrypting easy
        if item.isspace():
            result += item

        # ID alpha characters:
        elif item.isalpha():

            # Calling math function.
            # Calling .upper() function to deal with lower case inputs.
            indexLetter = alphabet.index(item.upper())
            # "-"  shift for decryption
            result += alphabet[(indexLetter - int(y)) % 26]

        else:
            print("Unwanted Character Found. Replaced with '.'")

    print("RESULT:",result)

# If user enters something other then 'E' or 'D'
else:
    print("Not an option provided")
