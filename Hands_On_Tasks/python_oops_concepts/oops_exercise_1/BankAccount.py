'''4. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, 
and methods like deposit, withdraw, and check_balance.'''

class BankAccount:
    
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        print(f"\nAccount Number : {self.account_number} \nCustomer Name : {self.customer_name} \nDate_of_opening : {self.date_of_opening} \nCurrent Balance : {self.balance}")
        
    def deposit(self, deposit_amount):
        deposit = self.balance + deposit_amount
        self.amount = deposit
        print(f"\nYou have deposited : {deposit_amount} \nYour Current Balance : {self.amount}") #14000
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.amount:
            withdraw = self.amount - withdraw_amount  # 14000 - 4000
            self.amount = withdraw
            print(f"\nYour withdrawal Amount : {withdraw_amount} \nYour Current Balance : {self.amount}") # 10000
        else:
            print("Insufficient Balance")
    
    def check_balance(self):
        print(f"\nYour Current Balance Amount : {self.amount}")
    
user = BankAccount("1234567890", 12000, "06-11-2024", "Sankar")
user.deposit(2000)
user.withdraw(4000)
user.check_balance()