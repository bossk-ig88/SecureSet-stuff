# SSF100 Python Lab 8b - Base Lab
# TRY 3: Base10 to any conversion: Base2, Base8, Base16.
#!/usr/bin/python3
import math
# user number output to "string".
number=""
# User input:  when user # is not a numeric.
while(not(number.isnumeric())):
    number = input("What is the decimal to convert? ")

# converts user number from "string" to "integer".
tempnumb = int(number)

# "binary" # outputs to a "string"
output =  ""

# conversion number outputs to a string.
base = ""

# string of value, for base systems > 10 (Base16).
values = "0123456789abcdefghijklmnopqrstuvwxyz"
values[] = ""


# when converted user "integer" is > 0:
while(tempnumb > 0):

    # User input: when user # is not a numeric:
    while(not(base.isnumeric())):
        base = input("Select Conversion: 2 for Base2, 8 for Base8, 16 for Base16: ")

    tempbase = int(base)
    # If conversion type from user = Base2
    if tempbase == 2:
        # Decimal to Base2 conversion:
        # User "integer" modulsed by 2
        # Converted to "string" and output added to result.
        def base10_to_Base2(dec):
            base10 = int(dec)

    if tempbase == 8:
        def base10_to_Base8():
            return str(tempnumb % 8) + output = output
            tempnumb = int(tempnumb / 8)

    if tempbase == 16:
        def base10_to_Base16():
            return str(tempnumb % 16) + output = output
            tempnumb = int(tempnumb / 16)

    if __name__ == '__main__':
        radius = int(input("What is the radius? "))
        print("The area is", area_of_circle(radius))
        print("The circumference is", circumference_of_circle(radius))


print(output)
