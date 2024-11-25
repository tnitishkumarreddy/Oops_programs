class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive")


    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance is {self.__balance}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")

    
    def get_balance(self):
        return self.__balance


account = BankAccount("Alice")
account.deposit(1000)
account.withdraw(500)
print(f"Current balance: {account.get_balance()}")
