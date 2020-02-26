# CRY100_01_Lab_Symmetric_Encryption
# ENCRYPT and DECRYPT capable (with "+" and "-" shifts for both)

# Using the above information, write a script
##that will take a plaintext and encrypt it
##using a Caesar cipher (shift 3 characters).
##Then write a corresponding decrypt script.
##Can you write one script that will do both?
##Can you write a script that will do any given rotation?

##print (25 % 3)
##myvar = 25 % 3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# User input:
question1 = input("'e' for Encrypt, 'd' for Decrypt: ")

# For Encyrption:
if question1 == "e":
    print("CHECK 1.a. start ENCYRPTION...")

    # 1. User Input:
    x = input("Plug in letter to ENCRYPT: ")

    # 2. User Cipher key shift:
    y = input("Plug in cipher key (numbers only): ")

    # 3. User Shift direction:
    sign = input("For encryption, '+' for postive shift: ")

    # Transform cipher key from string to integer:
    yint = int(y)


    # If "+" encryption shift:
    if sign == "+":
        print("CHECK 2. Caesar Cipher Ecryption")

        # Find the index of a specific letter:
        xIndex = alphabet.index(x)
        print("CHECK 2.i. Index number for user's letter =", xIndex)

        # 2. Cipher - shift ?? characters:
        caesarCipher = alphabet[(xIndex+yint) % 26]
        print("CHECK 2.ii. Encrption Shift = ", sign,yint)
        print("CHECK 2.FINAL.Encryption: ", x, "=", caesarCipher)


# For Decryption:
if question1 == "d":
    print("CHECK 1.b. start DECRYTPION...")

    # 1. User input:
    x = input("Plug in letter to DECRYPT: ")
    
    # 2. User Cipher key shift:
    y = input("Plug in cipher key (numbers only): ")

    # 3. User Shift direction:
    sign = input("For Decryption, '-' for negative shift: ")

    # Transform cipher key from string to integer:
    yint = int(y)


    # If "-" encryption shift:         
    if sign == "-":
        print("CHECK 5. Caesar Cipher Decryption")

        # Find the index of a specific letter:
        xIndex = alphabet.index(x)
        print("CHECK 5.i. Index number for user's letter =", xIndex)

        # 2. Cipher - shift ?? characters:
        caesarCipher = alphabet[(xIndex-yint) % 26]
        print("CHECK 5.iii. Decryption Shift = ", sign,yint)
        print("CHECK 5.Final. Decryption: ", x, "=", caesarCipher)

print("END OF LINE...")

