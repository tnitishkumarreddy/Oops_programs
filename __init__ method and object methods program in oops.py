class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_add='kizikistan'
    def __init__(self,cn,cac,cb):
        self.cname=cn
        self.account=cac
        self.bal=cb
    def customer_details(self):
        print(f'customer name is {self.cname}')
        print(f'customer account number is {self.account}')
        print(f'customer balance is {self.bal}')
    def withdraw(self):
        amount=int(input('enter the amount to withdraw'))
        if self.bal>amount:
            self.bal-=amount
            print(f'The remaining balance is {self.bal}')
            print('the withdraw is successful')
        else:
            print('Insufficient balance')
    def deposit(self):
        amount=int(input('enter the amount to deposit'))
        if amount>0:
            self.bal+=amount
            print('deposit is successful')
            print(f'The balance is {self.bal}')
        else:
            print('Enter the amount which is more than 0 rupees')
girish=Bank('Girish',2345,10000)
vishnu=Bank('Vishnu',4567,20000)

girish.customer_details()
Bank.customer_details(vishnu)
girish.withdraw()
vishnu.deposit()
        
