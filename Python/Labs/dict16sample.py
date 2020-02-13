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




result = 0
i = 0
while tempnumb != 0:
    # looking at each digit of the original decimal number one at a time,
    # from right to left, and multiplying it by 16 **
    # then adding it to the new number.
     result += (tempnumb % 10) * (16 ** i)
     tempnumb //= 10
     i += 1

print(tempnumb, result, "%x" % (result))
