from abc import ABC, abstractmethod

# Abstract class for a bank account
class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

# Concrete class for a savings account
class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to Savings Account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from Savings Account. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# Concrete class for a checking account
class CheckingAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to Checking Account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from Checking Account. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

savings = SavingsAccount("S12345", 1000)
checking = CheckingAccount("C12345", 2000)

savings.deposit(500)
savings.withdraw(200)
print(f"Savings Account Balance: {savings.get_balance()}")

checking.deposit(1000)
checking.withdraw(2500)
print(f"Checking Account Balance: {checking.get_balance()}")
