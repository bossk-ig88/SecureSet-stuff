##Then write a corresponding DECRYPt ONLY script.
##Can you write one script that will do both?
##Can you write a script that will do any given rotation?

##print (25 % 3)
##myvar = 25 % 3

# 1. User input:
x = input("Plug in letter: ")

# Cipher key shift:
y = input("Plug in cipher key (numbers only): ")

# Shift direction:
sign = input("For encryption, '+' for postive shift, '-' for negative shift: ")

# Transform cipher key from string to integer:
yint = int(y)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# If "+" encryption shift:
if sign == "+":
    
    # Find the index of a specific letter:
    xIndex = alphabet.index(x)
    print("CHECK 1. Index number for user's letter =", xIndex)

    # 2. Cipher - shift 3 characters:
    caesarCipher = alphabet[(xIndex+yint) % 26]
    print("CHECK 2. Caesar Cipher Ecryption")
    print("CHECK 2.i. Encrption Shift = ", sign,yint)
    print("CHECK 2.ii.Encryption: ", x, "=", caesarCipher)

# If "-" encryption shift:
if sign == "-":
    
    # Find the index of a specific letter:
    xIndex = alphabet.index(x)
    print("CHECK 1a. Index number for user's letter =", xIndex)

    # 2. Cipher - shift 3 characters:
    caesarCipher = alphabet[(xIndex-yint) % 26]
    print("CHECK 3. Caesar Cipher Ecryption")
    print("CHECK 3.i. Encrption Shift = ", sign,yint)
    print("CHECK 3.ii.Encryption: ", x, "=", caesarCipher)

print("END OF LINE...")
