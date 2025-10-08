''' Design a simple calculator with basic arithmetic operations.Prompt the user to input 
two numbers and an operation choice. Perform the calculation and display the result. '''


from Function_Calculator import *

while True:
    print("What do you want to do ??")
    print("Press 1 : For Addition")
    print("Press 2 : For Subtration")
    print("Press 3 : For Multiplication")
    print("Press 4 : For Division")
    print("Enter x to Exit the program")

    choice = input("Please enter your choice : ")
    if choice == 'x' or choice == 'X':
        break
    num1 = float(input("Enter your First Number : "))
    num2 = float(input("Enter your Second Number : "))

    if choice == "1":
        add(num1,num2)
    elif choice == "2":
        subtract(num1,num2)
    elif choice == "3":
        multiply(num1,num2)
    elif choice == "4":
        division(num1,num2)
    else:
        print("Sorry, Invalid Result. Please try again.")

    print("\n") # we use this for creating a gap b/w 2 operation.