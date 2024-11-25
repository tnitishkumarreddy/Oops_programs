class Bank:
    bank_name='SBI'
    bank_ifsc=1234
    bank_branch='kizikistan'
    bank_roi=7
    def __init__(self,cn,ca,cb,cacc):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
        self.caccount=cacc

    @classmethod
    def bank_details(cls):
        print(f'The bank name is:{cls.bank_name}')
        print(f'The bank ifsc number is:{cls.bank_ifsc}')
        print(f'The bank branch name is:{cls.bank_branch}')
    def customer_details(self):
        print(f'The customer name is:{self.cname}')
        print(f'The customer age is:{self.cage}')
        print(f'The customer account balance is:{self.cbal}')
        print(f'The customer account number is:{self.caccount}')

    @staticmethod
    def get_int_value():
        iv=int(input('enter the value'))
        return iv
    def withdraw(self):
        amount=self.get_int_value()
        if self.cbal>amount:
            self.cbal-=amount
            print(f'The amount of rupees {amount} is withdrawl successfully')
            print(f'The remaining balance in the account is:{self.cbal}')
        else:
            print('Insufficient balance')
    def deposit(self):
        amount=self.get_int_value()
        if amount>0:
            self.cbal+=amount
            print(f'Amount of rupees {amount} is deposit successfully')
            print(f'The total amount in the account is:{self.cbal}')
        else:
            print('Enter the valid amount to deposit')

    @staticmethod

    def get_str_value():
        sv=input('enter value')
        return sv
    
    @classmethod
    def change_roi(cls):
        new_roi=cls.get_int_value()
        cls.bank_roi=new_roi
        print('The rate of interest is modified')
        print(f'The new rate of interest is:{cls.bank_roi}')
    @classmethod
    def change_branch(cls):
        new_branch=cls.get_str_value()
        cls.bank_branch=new_branch
        print('The branch is modified')
        print(f'The new branch name is:{cls.bank_branch}')

Nitish=Bank('Tatigotla Nitish',23,50,1234)
jai=Bank('Kamireddy JaiPall',22,6450,2345)
Teja=Bank('GangiReddy Teja Nanda reddy',21,457,3456)


Nitish.bank_details()
Nitish.customer_details()
Nitish.withdraw()
Nitish.deposit()

