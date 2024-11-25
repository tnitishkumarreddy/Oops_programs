class IncorrectPin(BaseException):
    def __init__(self):
        print('Incorrect pin')


class InsufficientBalance(BaseException):
    def __init__(self):
        print('Insufficient Balance')

def singleton(arg):

    l=[]
    def inner():
        if not l:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner

@singleton
class withdraw:

    def __init__(self):

        self.name='Nitish'
        self.bal=3000
        self.pin=1111

    def withdrawl(self):
        ep=int(input('Enter the pin:'))
        try:
            if ep!=self.pin:
                raise IncorrectPin
            amt=int(input('Enter the amount:'))

            try:
                if amt>self.bal:
                    raise InsufficientBalance
                self.bal-=amt
                print(f'Amount of rupees {amt} is withdrawl successfully')
                print(f'The remaining balance in the account is {self.bal}')
            except Insufficientbalance as e:
                print(e)

        except IncorrectPin as b:
            print(b)
    def deposite(self):
        amt=int(input('Enter the amount to deposit:'))
        self.bal+=amt
        print(f'The amount is deposited successfully')
        print(f'The remaining balance in the account is:{self.bal}')


user1=withdraw()
user1.withdrawl()
user1.deposite()




        

        
    
