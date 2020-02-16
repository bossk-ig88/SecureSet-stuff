# simple calculator
import math
# Math Definitions
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

# User input
userinput = input("Enter equation:")
print("CHECK 1. User input = ", userinput)

# FIND OPERATORS:
# Add
findOPadd = userinput.find("+")
print("CHECK 1.i. Add Op is in slot:", findOPadd)
# Subtract
findOPminus = userinput.find("-")
print("CHECK 1.ii. Minus Op is in slot:", findOPminus)
# Multiply
findOPtimes = userinput.find("*")
print("CHECK 1.iii. Times Ops is in slot:", findOPtimes)
# Divide
findOPdivide = userinput.find("/")
print("CHECK 1.iv. Divide Ops is in slot:", findOPdivide)

# If OPERATOR = "+" in SLOT 1:
if  findOPadd == 1:
    print("CHECK 2. Add operator,", findOPadd)

    # select stringed index to left of operator
    x = userinput[findOPadd-1]
    print("CHECK 2.i. User Number 1 =", x)
    # Convert string into integer.
    num1 = int(x)
    print("CHECK 2.ii. Number 1 converted to integer =", num1)

    # select stringed index to right of operator
    y = userinput[findOPadd+1]
    print("CHECK 2.iii. User Number 2 =", y)
    # Convert string into integer.
    num2 = int(y)
    print("CHECK 2.iiv. User Number 2 converted to integer=", num2)
    # Adding integers:
    print("CHECK 2.FINAL.",num1,"+",num2, "=", add(num1,num2))

# If OPERATOR = "-" in SLOT 1:
elif  findOPminus == 1:
    print("CHECK 3. Minus operator,", findOPminus)

    # select stringed index to left of operator
    x = userinput[findOPminus-1]
    print("CHECK 3.i. User Number 1 =", x)
    # Convert string into integer.
    num1 = int(x)
    print("CHECK 3.ii. Number 1 converted to integer =", num1)

    # select stringed index to right of operator
    y = userinput[findOPminus+1]
    print("CHECK 3.iii. User Number 2 =", y)
    # Convert string into integer.
    num2 = int(y)
    print("CHECK 3.iiv. User Number 2 converted to integer=", num2)
    # Subtract integers:
    print("CHECK 3.FINAL.",num1,"-",num2, "=", subtract(num1,num2))

elif  findOPtimes == 1:
    print("CHECK 4. Times operator,", findOPtimes)

    # select stringed index to left of operator
    x = userinput[findOPtimes-1]
    print("CHECK 4.i. User Number 1 =", x)
    # Convert string into integer.
    num1 = int(x)
    print("CHECK 4.ii. Number 1 converted to integer =", num1)

    # select stringed index to right of operator
    y = userinput[findOPtimes+1]
    print("CHECK 4.iii. User Number 2 =", y)
    # Convert string into integer.
    num2 = int(y)
    print("CHECK 4.iiv. User Number 2 converted to integer=", num2)
    # Multiply integers:
    print("CHECK 4.FINAL.",num1,"*",num2, "=", multiply(num1,num2))

elif  findOPdivide == 1:
    print("CHECK 5. Times operator,", findOPdivide)

    # select stringed index to left of operator
    x = userinput[findOPdivide-1]
    print("CHECK 5.i. User Number 1 =", x)
    # Convert string into integer.
    num1 = int(x)
    print("CHECK 5.ii. Number 1 converted to integer =", num1)

    # select stringed index to right of operator
    y = userinput[findOPdivide+1]
    print("CHECK 5.iii. User Number 2 =", y)
    # Convert string into integer.
    num2 = int(y)
    print("CHECK 5.iiv. User Number 2 converted to integer=", num2)
    # Divide integers:
    print("CHECK 5.FINAL.",num1,"*",num2, "=", divide(num1,num2))

else:
    print("CHECK 6. PUNT!!! You invalid!")

print("END OF LINE...")
