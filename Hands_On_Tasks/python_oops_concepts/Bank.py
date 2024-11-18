class Bank:
    bank_name = "HDFC Bank"
    bank_location = "KK Nagar"
    customer_care = "1800-12345-678"
    
    customer_name = "Kiruba"
    account_balance = 0.0
    account_number = 00000
    
    alternate = "self"

    def __init__(self):
        print("I'm super class __init__")
    
    def working(self):
        print(f"Today {self.bank_name} is Available")

class Bank_Account(Bank):
    # customer_name = "Kiruba"
    # account_balance = 0.0
    # account_number = 00000
    
    def __init__(self, customer_name, account_balance, account_number, alternate):
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.account_number = account_number
        self.alternate = alternate
    
    def check_balance(self):
        print(f"Hi {self.customer_name},\nYour Account balance : {self.account_balance} in {self.bank_name} @ {self.bank_location}\nPlease contact us : {self.customer_care}")
        
    def statement(self):
        print(f"Hi {self.customer_name},\nYour Account Balance : {self.account_balance}\nYour Account Number : {self.account_number}")
        
    def __del__(self):
        print("Bank_Account Destructor", self)
    
    def __str__(self):
        return(self.alternate)

bank_details = Bank_Account("Shiva", 100, 1234576576, "instead_of_self")
bank_details.check_balance()

print(bank_details)
# bank = Bank()
# bank.working()
