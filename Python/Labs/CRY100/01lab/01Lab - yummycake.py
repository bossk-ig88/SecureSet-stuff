# CRY100 - 01 Lab - CAKE IS YUMMY section
# Only do encryption and + shift...for testing.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# User input:
question1 = input("'E' for Encrypt, 'D' for Decrypt: ")

caesarCipher = []

result = ""

indexLetter = []


# For Encyrption:
if question1 == "E":
    print("Start ENCYRPTION...")

    x=""

    # 1. User Input:
    x = input("ENCRYPT (only caps): ")
    
    # 2. User Cipher key shift:
    y = input("Plug in cipher key (numbers only): ")

    # Transform cipher key from string to integer:
    yint = int(y)

    # checking whether whitespace is present  
    userSpace = x.isspace()        
    print("1. Value result:", userSpace)

    if userSpace == False:
        splitX = x.split()
        print("2. Split items:", splitX)
        
        # Find length of list and then iterate over it by
        # using len() function.
        # Length output is range.
        print("3. Start Loop.")
        for item in range(len(splitX)):
            itemSplitX = splitX[item]
            print("4. Iterated item (word) in list:", itemSplitX)

            # Loop through each split word, and iterate through each letter:
            for letter in itemSplitX:
                # Indexed each individual letter:

                indexLetter = alphabet.index(letter)
                print("5. (Letter=Index):", letter, " = ", indexLetter)
            
                caesarCipher = alphabet[(indexLetter+yint) % 26]
                print("5.i. Encryption Shift = +", yint)

                print("5.ii. (Letter=Encrypted):", letter, "=", caesarCipher)

                # Add encrypted letters together (but no spaces):
                for lett in caesarCipher:
                    result += lett
                print("RESULT:", result)
