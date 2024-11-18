'''Polymorphism - One object can perform multiple tasks'''

# Method Overloading
class Calculator:
    
    def add(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
    
        total = first_value + second_value
        print(f"The addition of {self.first_value} and {self.second_value} : ",total)
        
    def subtract(self, first_value, *args):
        self.first_value = first_value
        value = first_value
        for number in args:
            value = value + number 
        total = value
        print(f"The addition of {self.first_value} and {args} : ",total)
        
addition = Calculator()
addition.add(10, 20)
addition.subtract(100, 80, 80, 1)