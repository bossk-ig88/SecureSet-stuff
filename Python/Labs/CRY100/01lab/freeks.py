#!/usr/bin/python3

txtfile = open("/Users/bossman1/Documents/GIT/SecureSet-stuff/Python/Labs/CRY100/CRY100_01_Lab_Substitution.txt","r")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# read text file
txt = txtfile.read()


# for letter in alphabet:
for letter in alphabet:
    #Count total letters in text file:
    print(letter, "-", txt.count(letter))
    # Get the percentage. 
    # (total count of letters)/(total letters) * 100
    freq = txt.count(letter)/len(txt) * 100
    # round off to 1 decimal point using float
    freeks = (round(float(freq), 1))
    print("Percentage -", freeks, "%")
    
print("Total letters in text file:", len(txt))
# Close files that we opened
txtfile.close()

