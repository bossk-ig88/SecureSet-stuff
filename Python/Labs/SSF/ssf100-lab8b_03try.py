# # SSF100 Python Lab 8b - Base Lab
# TRY 3: Base10 to any conversion: Base2, Base8, Base16.
#!/usr/bin/python3
import math
# user number output to "string".
number=""
# User input:  when user # is not a numeric.
while(not(number.isnumeric())):
    print("1. LOOP 1: START.")  # PRINT CHECK
    number = input("1.i. What is the decimal to convert? ")
# converts user number from "string" to "integer".
tempnumb = int(number)
print("1.ii. Pre-2 Loop: Temp 'User' Number to integer= " + str(tempnumb))
# "binary" # outputs to a "string"
output =  ""
# conversion number outputs to a string.
base = ""
# Hex dictionary
hexdict = {}
# Hex values to be matched with a key in a dictionary
values = "0123456789abcdef"


for key, value in letters.items():
    # displays key matched with numerical value
    print (key + " = " + str(value))

print(hexdict)



# User input: when user # is not a numeric:
while(not(base.isnumeric())):
    base = input("2. LOOP 2: Select Conversion: 2 for Base2, 8 for Base8, 16 for Base16 = ")
# converts user number from "string" to an "integer".
tempbase = int(base)
print("2.i. Temp Base Number = " + str(tempbase))
# If conversion type from user = Base2
if tempbase == 2:
    print("3. IF 1: START.")
    print("3.i. temp base = " + str(tempbase))
    # when converted user "integer" is > 0:
    while(tempnumb > 0):
        print("4. LOOP 3: START.")  # PRINT CHECK
        print("4.i. Temp 'User' Number = " + str(tempnumb))
        # User "integer" modulsed by 2
        # Converted to "string" and output added to result.
        output = str(tempnumb % 2) + output
        print("4.ii. Start conversion: current answer = " + str(output))
        # user integer / 2 and converted to binary
        tempnumb = int(tempnumb / 2)
        print("4.iii. Final conversion: remainder =  " + str(tempnumb))

# If conversion type from user = Base8
if tempbase == 8:
    print("5. IF (2): START.")
    print("5.i. temp base = " + str(tempbase))
    # when converted user "integer" is > 0:
    while(tempnumb > 0):
        print("6. LOOP 3: START.")  # PRINT CHECK
        print("6.i. Temp 'User' Number = " + str(tempnumb))
        # User "integer" modulsed by 8
        # Converted to "string" and output added to result.
        output = str(tempnumb % 8) + output
        print("6.ii. Start conversion: current answer = " + str(output))
        # user integer / 8 and converted to binary
        tempnumb = int(tempnumb / 8)
        print("6.iii. Final conversion: remainder =  " + str(tempnumb))

# If conversion type from user = Base16
if tempbase == 16:
    print("7. If (3): START.")
    print("7.i. temp base = " + str(tempbase))
    while(tempnumb > 0):
        print("8. LOOP 3: START.")  # PRINT CHECK
        print("8.i. Temp 'User' Number = " + str(tempnumb))
        # User "integer" modulsed by 16
        # Converted to "string" and output added to result.
        output = str(tempnumb % 16) + output
        print("8.ii. Start conversion: current answer = " + str(output))
        # user integer / 16 and converted to binary
        tempnumb = int(tempnumb / 16)
        print("8.iii. Final conversion: remainder =  " + str(tempnumb))

print("Final Result = " + output)
print("End of Line...")
