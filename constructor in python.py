class Bank:
    bank_name='sbi'
    bank_ifsc=345
    bank_add='kiwi'
    def __int__(self,cn,ca,cb):
        self.cname=cn
        self.acc=ca
        self.bal=cb
girish=Bank('Girish',3456,10000)
vishnu=Bank('Vishnu',234,200000)
print(girish.cname,vishnu.bal)
