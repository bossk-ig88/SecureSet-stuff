# # SSF100 Python Lab 8a
# # Base Lab
# TRY 1: Decimal >> Binary  Lab.
#!/usr/bin/python3
import math

# user number output to "string".
number=""

# User input:
# when user # is not a numeric.
# Will run/execute loop (ask user) until defined condition is met.
# .isnumeric() = is a string method that checks whether
# the string consists of only numeric characters.
while(not(number.isnumeric())):
    number = input("What is the decimal to convert? ")

# converts user number from "string" to an "integer".
tempnumb = int(number)

# "binary" # outputs to a "string"
bin_output = ""

# when converted user "integer" is > 0:
while(tempnumb > 0):
    print("CHECK 1 = start of While loop.")  # PRINT CHECK

    # Decimal to binary  conversion:
    # user "integer" modulused by 2 and
    # result is converted to "string" and bin_output is added to result.
    bin_output = str(tempnumb % 2) + bin_output
    print("CHECK 2 = start conversion. " + str(bin_output))

    # user integer / 2 and converted to binary
    tempnumb = int(tempnumb / 2)
    print("CHECK 3 = final conversion. " + str(tempnumb))

print (bin_output)
print("End of Line...")
