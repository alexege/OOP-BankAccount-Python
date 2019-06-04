class BankAccount:
    
    def __init__(self, interest_rate, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance - amount
        else:
            print("Insufficient funds!")
        return self        

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0 :
            self.balance += self.balance * self.interest_rate
        else:
            print("Balance is negative")
        return self        

# Create 2 accounts 
account1 = BankAccount(0.01)
account2 = BankAccount(0.02, 100)

# Make 3 deposits in the first account, 1 withdrawal, and calculate the interest and display the account's info in one line
account1.deposit(200).deposit(100).deposit(50).withdrawal(150).yield_interest().display_account_info()

# Make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code
account2.deposit(100).deposit(200).deposit(300).deposit(400).yield_interest().display_account_info()

