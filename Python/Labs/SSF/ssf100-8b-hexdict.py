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

# Hex values
values = "0123456789abcdef"
result = 0
i = 0
# tempnumb subbed in for orig = num.
# User input: when user # is not a numeric:
while(not(base.isnumeric())):
    base = input("2. LOOP 2: Select Conversion: 2 for Base2, 8 for Base8, 16 for Base16 = ")
# converts user number from "string" to an "integer".
tempbase = int(base)
print("2.i. Temp Base Number = " + str(tempbase))
# If conversion type from user = Base16
if tempbase == 16:
    print("7. If (3): START.")
    print("7.i. temp base = " + str(tempbase))
    while(tempnumb > 0):
        print("8. LOOP 3: START.")  # PRINT CHECK
        print("8.i. Temp 'User' Number = " + str(tempnumb))

        result += (tempnumb % 10) * (16 ** i)
        tempnumb //= 10
        i += 1

    print(tempnumb, result, "%x" % (result))

        # # User "integer" modulsed by 16
        # # Converted to "string" and output added to result.
        # output = str(tempnumb % 16) + output
        # print("8.ii. Start conversion: current answer = " + str(output))
        # # user integer / 16 and converted to binary
        # tempnumb = int(tempnumb / 16)
        # print("8.iii. Final conversion: remainder =  " + str(tempnumb))

print("Final Result = " + output)
print("End of Line...")



        # for num in tempnumb:
        #      #Checks if number in dictionary exists.
        #     if num in hexdict.keys():
        #         # Adds a value of 1 (increase of occurance of letter by user)
        #         # for that letter and assigns that new value to that key location in dictionary
        #         hexdict[num] += 1
        #         # If letter exists in dictionary already, value remains at 1 (unchanged):
        #     else:
        #         hexdict[num]=1
        # for key, value in hexdict.items():
        #     # displays key matched with numerical value
        #     print (key + " = " + str(value))

                # print(hexdict)
