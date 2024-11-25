'''class Address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_address(self):
        print(f'The student city is:{self.city}')
        print(f'The student state is:{self.state}')
        print(f'The studenmt country is:{self.country}')
obj=Address('Bang','kar','Ind')


class Student:
    def __init__(self,sn,sa,sc,ad):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        self.saddress=ad

    def student_info(self):
        print(f'The student name is:{self.sname}')
        print(f'The student age is:{self.sage}')
        print(f'The student class is:{self.sclass}')
        print(f'The student address is :')
        self.saddress.display_address()
niti=Student('Nitish',23,'Python',obj)
niti.student_info()

'''



class Address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_address(self):
        print(f'The student city is:{self.city}')
        print(f'The student state is:{self.state}')
        print(f'The studenmt country is:{self.country}')



class Student:
    def __init__(self,sn,sa,sc):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        c=input('Enter the city name:')
        s=input('Enter the state name:')
        co=input('Enter the country name:')
        addrobj=Address(c,s,co)
        self.saddress=addrobj

    def student_info(self):
        print(f'The student name is:{self.sname}')
        print(f'The student age is:{self.sage}')
        print(f'The student class is:{self.sclass}')
        print(f'The student address is :')
        self.saddress.display_address()
niti=Student('Nitish',23,'Python')
niti.student_info()
