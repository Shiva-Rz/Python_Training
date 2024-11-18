''' Implement a simple command-line calculator that can perform basic arithmetic operations 
    such as addition, subtraction, multiplication, and division. 
    
- The calculator should be able to handle multiple operations in a single session, allowing the user to 
- choose whether to continue calculating with the result of the previous operation or start a new calculation. 

The calculator should also handle invalid operator inputs and provide a clear and user-friendly interface.'''

class Calculator:
    
    def operations(self, first_value, second_value, operator):
            
            if operator == '+':
                total = first_value + second_value
                print(f"\nAddition of {first_value} {operator} {second_value} =", total)
                return first_value + second_value
            elif operator == '-':
                total = first_value - second_value
                print(f"\nSubtraction of {first_value} {operator} {second_value} =", total)
                return first_value - second_value
            elif operator == '*':
                total = first_value * second_value
                print(f"\nMultiplicaton of {first_value} {operator} {second_value} =", total)
                return first_value * second_value
            elif operator == '/':
                total = first_value / second_value
                print(f"\nDivision of {first_value} {operator} {second_value} =", total)
                return first_value / second_value
            else:
                print("Please Enter valid operator")
                

    def processing(self):
        
        first_value = int(input("\nEnter the First Value : "))
        
        while True:
            
            print("\nEnter any one of the operator : \nAddition : + \nSubtraction : - \nMultiplication : * \nDivision : / ")
            operator = input("\nEnter any one of the operator from the above : ")

            second_value = int(input("Enter the Second Value : "))
        
            first_value = self.operations(first_value, second_value, operator)
            
            condition = input("\nEnter 'Yes'/'y' to Continue \nEnter 'No'/'n' to terminate : ")
            
            if condition.lower() == 'No' or condition.lower() == 'n':
                print("Your calculation is Terminated")
                break

calculation = Calculator()              
calculation.processing()
