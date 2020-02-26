##CRY100-1 Lab - Substitution Cipher:
##Frequency Analysis Results
##Frequency Analysis methodology (python code, spreadsheet or
##the amount of time it took to count them manually).
##Plaintext
##So, the first step is to perform a frequency analysis
##on the substitution.txt file by determining
##how many of each letter exists in the text.

txtfile = ""

txtfile = open("/Users/bossman1/Documents/GIT/SecureSet-stuff/Python/Labs/CRY100/CRY100_01_Lab_Substitution.txt","r")

stringtxtfile = txtfile.read()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

count = 0

# for letter in alphabet:
for alpha in alphabet:
    # Count alphas in alphabet:
    alphaCounter = alphabet.count("")

    # for letter in text file:
    for letter in stringtxtfile:
        # Count total letters in text file:
        totalLetterCount = stringtxtfile.count("")
        # if letter in text file is in the alphabet:
        if letter in alphabet:
            # Add count in "letterCount" Dictionary:
            letterCount[letter] += 1

        
#print("Total number in alphabet:", alphaCounter)
print("Total letters in text file:", totalLetterCount)
print("Occurance of each letter in the text file = ", letterCount)

#print(letterCount.values())
#percentDict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
##
##for value in letterCount.values():
##    frequency = (value / totalLetterCount)*100
##    percentage = (round(float(frequency), 2))
##    print(percentage,"%")
##    
##for key in (letterCount.keys()):
##    print(key, "=", percentage)
        

