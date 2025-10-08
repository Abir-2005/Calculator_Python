# we use this file for writing the function which is used for making calculator.

def add(num1, num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1,num2,result))

def subtract(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1,num2,result))

def multiply(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1,num2,result))

def division(num1, num2):
    if num2 == 0:
        print("Sorry.... We can't Perform this.")
    else :
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1,num2,result))