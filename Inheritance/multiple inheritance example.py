class sql:
    course_name='SQL'
    trainer_name='Jyoshna'
    no_of_classes_taken=39
    def __init__(self,sn,sm,nca,smr):
        self.sname=sn
        self.smobile=sm
        self.no_of_classes_attended=nca
        self.smock=smr
        self.student_sql_details()
        self.sql_course_details()
    @classmethod
    def sql_course_details(cls):
        print(f'course name is:{cls.course_name}')
        print(f'The trainer of the course {cls.course_name} is:{cls.trainer_name}')
        print(f'The number of classes taken for the course {cls.course_name} is:{cls.no_of_classes_taken}')
        

    def student_sql_details(self):
        print(f'student name is:{self.sname}')
        print(f'{self.sname} mobile number is:{self.smobile}')
        print(f'The number of classes attend by {self.sname} is {self.no_of_classes_attended}')
        print(f'{self.sname} mock rating in sql is:{self.smock}')

class python:
    course_name='Python'
    trainer_name='Harshad'
    no_of_classes_taken=90
    def __init__(self,ca,new_smr):
        self.no_of_classes_attended=ca
        self.new_mock=new_smr
        self.student_python_details()
        self.python_course_details()

    @classmethod
    def python_course_details(cls):
        print(f'course name is:{cls.course_name}')
        print(f'The trainer of the course {cls.course_name} is:{cls.trainer_name}')
        print(f'The number of classes taken for the course {cls.course_name} is:{cls.no_of_classes_taken}')
        
    def student_python_details(self):
        print(f'The no of classes attended:{self.no_of_classes_attended}')
        print(f'student mock rating in python is:{self.new_mock}')
        


class student(sql,python):
    print('The entire student details are:')

    def __init__(self):
        student_name=input('Enter the student name:')

        student_mobile_number=int(input('Enter the mobile number of the student:'))

        no_of_sql_classes_attended=int(input('Enter the number of classes attended for sql:'))

        sql_mock=input('Enter the sql mock rating of the student:')
        
        no_of_python_classes_attended=int(input('Enter the number of classes attended for python:'))

        python_mock=input('Enter the python mock rating of the student:')
        
        sql(student_name,student_mobile_number,no_of_sql_classes_attended,sql_mock)

        python(no_of_python_classes_attended,python_mock)

s1=student()


