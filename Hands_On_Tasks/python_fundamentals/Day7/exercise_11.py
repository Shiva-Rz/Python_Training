'''Implement a simple command-line calculator that can perform basic arithmetic operations 
such as addition, subtraction, multiplication, and division. 
    - The calculator should be able to handle multiple operations in a single session, allowing the user to 
    - choose whether to continue calculating with the result of the previous operation or start a new calculation. 
    The calculator should also handle invalid operator inputs and provide a clear and user-friendly interface.''' 

# Write a Python program that meets these requirements

def calculator():
    
    first_number = int(input("\nEnter the Number : "))
    
    while True:
        operators = ['+', '-', '*', '/']

        print("Choose any one of the Operator from the below \n")
        
        for symbol in operators:
            print(symbol)

        operation = input("\nSelect the operator type : ")

        second_number = int(input("\nEnter the Number : "))

        if operation == '+':
            total = first_number + second_number
            print(f"The value {first_number} + {second_number} =", total)
        elif operation == '-':
            total = first_number - second_number
            print(f"The value {first_number} - {second_number} =", total)
        elif operation == '*':
            total = first_number * second_number
            print(f"The value {first_number} * {second_number} =", total)
        elif operation == '/':
            total = first_number / second_number
            print(f"The value {first_number} - {second_number} =", total)
        else:
            print("You have entered Invalid Operator")
        first_number = total

        condition = input("If you want to continue type : 'yes or y' else type : 'no or n' : ")

        if condition.lower() == 'no' or condition == 'n':
            print("The process successfully completed")
            break

calculator()