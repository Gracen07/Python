class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs. {amount}. New balance: Rs. {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew Rs. {amount}. New balance: Rs. {self.balance}")
        else:
            print("Insufficient balance.")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: Rs. {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.5):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Interest calculated. New balance: Rs. {self.balance}")

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew Rs. {amount}. New balance: Rs. {self.balance}")
        else:
            print("Exceeded overdraft limit.")



def main():
    
    savings_account = SavingsAccount("GKS123", 15000, 1.0)
    savings_account.display_balance()
    savings_account.deposit(2000)
    savings_account.calculate_interest()
    savings_account.withdraw(3000)
    savings_account.display_balance()

    print("\n")

    
    current_account = CurrentAccount("GKS456", 100000, 2000)
    current_account.display_balance()
    current_account.deposit(5000)
    current_account.withdraw(15000)
    current_account.display_balance()

if __name__ == "__main__":
    main()
