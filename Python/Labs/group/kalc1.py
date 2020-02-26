# simple calculator
import math
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
num1,ops,num2 = [input('Enter your equation:').split()]
print('Your answer is:', result)
if ops == '+':
    print(num1,"+",num2, "=", add(num1,num2))
elif ops == '-':
    print(num1, "-", num2, "=",
                    subtract(num1, num2))
elif ops == '*':
    print(num1, "*", num2, "=",
                    multiply(num1, num2))
elif ops == '/':
    print(num, "/", num2, "=",
                    divide(num1, num2))
else:
    print("Invalid input")
