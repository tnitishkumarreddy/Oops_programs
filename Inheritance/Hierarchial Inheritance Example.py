class Jspiders:
    Institute_name='Jspiders'
    type='software training institute'

    def __init__(self):
        self.jspiders_details()
        print('The courses that are available in jspiders are:')
        print('Java Full Stack')
        print('Python Full Stack')
        print('Mern stack')
        print('Software testing')

        

    @classmethod
    def jspiders_details(cls):
        print(f'The institute name is:{cls.Institute_name}')
        print(f'{cls.Institute_name} is a {cls.type}')

class Jspiders_marathahalli(Jspiders):
    b=Jspiders.Institute_name
    branch_name=b+' '+'Marathahalli'
    address='Near KLM Mall,Marathahalli,Banglore'
    python_trainers_marathahalli='Harshad and pranay'
    django_trainer_marathahalli='Harshad'
    sql_trainers_marathahalli='Greeshma and Ankitha'
    java_trainers_marathahalli='Raveesh and Ramana'
    web_trainers_marathahalli='Kishore and Dhruva'

    def __init__(self):
        Jspiders()
        self.marathahalli_details()
        

    @classmethod
    def marathahalli_details(cls):
        print('                                                                       ')
        print(f'The branch name is:{cls.branch_name}')
        print(f'Address of jspiders {cls.branch_name} is:{cls.address}')
        print(f'Python trainers in jspiders marathahalli branch are:{cls.python_trainers_marathahalli}')
        print(f'SQL trainers in jspiders marathahalli branch are:{cls.sql_trainers_marathahalli}')
        print(f'Django trainer in jspiders marathahalli branch are:{cls.django_trainer_marathahalli}')
        print(f'Java trainers in jspiders marathahalli branch are:{cls.java_trainers_marathahalli}')
        print(f'web technology trainers in jspiders marathahalli are:{cls.web_trainers_marathahalli}')


class Jspiders_BTM(Jspiders):
    a=Jspiders.Institute_name
    branch_name=a+' '+'BTM layout'
    address='J.P.Nagar,BTM layout,Banglore'
    python_trainers_btm='Ramesh and Suresh'
    django_trainer_btm='Harshad'
    sql_trainers_btm='sudha and radha'
    java_trainers_btm='Teja and Raja'
    web_trainers_btm='Tarun and Arun'

    def __init__(self):
        Jspiders()
        self.btm_details()
        

    @classmethod
    def btm_details(cls):
        print('                                                                       ')
        print(f'The branch name is:{cls.branch_name}')
        print(f'Address of jspiders {cls.branch_name} is:{cls.address}')
        print(f'Python trainers in jspiders btm layout branch are:{cls.python_trainers_btm}')
        print(f'SQL trainers in jspiders btm layout branch are:{cls.sql_trainers_btm}')
        print(f'Django trainer in jspiders btm layout branch are:{cls.django_trainer_btm}')
        print(f'Java trainers in jspiders btm layout branch are:{cls.java_trainers_btm}')
        print(f'web technology trainers in jspiders btm layout are:{cls.web_trainers_btm}')

stu1=Jspiders_BTM()

print('                                                                   ')

stu2=Jspiders_marathahalli()
    
    
        
