class Bank1:
    bank_name='SBI'
    bank_ifsc=1234
    bank_branch='Banglore'

    def __init__(self,cn,ca,cacc,cbal):
        self.cname=cn
        self.cage=ca
        self.caccount=cacc
        self.cbalance=cbal

    @classmethod
    def bank_details(cls):
        print(f'The bank name is: {cls.bank_name}')
        print(f'The bank ifsc is: {cls.bank_ifsc}')
        print(f'The bank branch is: {cls.bank_branch}')

    def customer_details(self):
        print(f'Customer name is: {self.cname}')
        print(f'Customer age is: {self.cage}')
        print(f'Customer account number is: {self.caccount}')
        print(f'Customer balance is: {self.cbalance}')

    def withdraw(self):
        amount=int(input('Enter the amount to withdraw:'))
        if self.cbalance>amount:
            self.cbalance-=amount
            print(f'The amount of rupees {amount} is withdrawl successfully')
            print(f'The remaining balance in the account is:{self.cbalance}')
        else:
            print('Insufficient balance')
    def deposit(self):
        amount=int(input('Enter the amount to deposit:'))
        if amount>0:
            self.cbalance+=amount
            print(f'Amount of rupees {amount} is deposit successfully')
            print(f'The total amount in the account is:{self.cbalance}')
        else:
            print('Enter the valid amount to deposit')


class Bank2(Bank1):
    bank_branch='Hyderabad'    #property overriding
    bank_roi=7

    def __init__(self,cn,ca,cacc,cbal,cp):
        super().__init__(cn,ca,cacc,cbal)
        self.cpin=cp

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f'Bank roi is:{cls.bank_roi}')

    def withdraw(self):
        ep=int(input('Enter the pin:'))
        if ep==self.cpin:
            super().withdraw()
        else:
            print('Incorrect pin')
    
    @classmethod
    def change_roi(cls):
        new_roi=int(input('Enter the new roi value:'))
        cls.bank_roi=new_roi
        print('The rate of interest is modified')
        print(f'The new rate of interest is:{cls.bank_roi}')
    @classmethod
    def change_branch(cls):
        new_branch=input('Enter the new branch name:')
        cls.bank_branch=new_branch
        print('The branch is modified')
        print(f'The new branch name is:{cls.bank_branch}')


Nitish=Bank2('Tatigotla Nitish',23,1569,17,2024)
Nitish.bank_details()
Nitish.customer_details()
Nitish.deposit()
Nitish.withdraw()

        

        
        
