class Engineering:
    college_name='ABC'
    type_of_graduation='Under Graduation'
    time='4 years'
    no_of_sems=2

    def __init__(self):
        self.details()

    @classmethod
    def details(cls):
        print(f'The student college name is:{cls.college_name}')
        print(f'The student graduation type is:{cls.type_of_graduation}')
        print(f'The time period for completing the graduation is:{cls.time}')
        print(f'The no of semesters in the graduation is:{cls.no_of_sems}')

class ECE(Engineering):

    branch='ECE'
    hod_name='Harshad'

    def __init__(self):
        Engineering()
        print('                      ')
        self.ece_department_details()
        for i in range(1,self.no_of_sems+1):
            no_of_sub=int(input(f'Enter the no_of_subjects in {i} semester:'))
            print(f'The no of subjects in {i} semester are:{no_of_sub}')
            no_of_labs=int(input(f'Enter the no_of_labs in {i} semester:'))
            print(f'The no of labs in {i} semester are:{no_of_labs}')

    @classmethod
    def ece_department_details(cls):
        print(f'The department name is:{cls.branch}')
        print(f'The HOD of the department {cls.branch} is:{cls.hod_name}')


class CSE(Engineering):

    branch='CSE'
    hod_name='Raveesh'

    def __init__(self):
        Engineering()
        print('                       ')
        self.cse_department_details()

        for i in range(1,self.no_of_sems+1):
            no_of_sub1=int(input(f'Enter the no_of_subjects in {i} semester:'))
            print(f'The no of subjects in {i} semester are:{no_of_sub1}')
            no_of_labs1=int(input(f'Enter the no_of_labs in {i} semester:'))
            print(f'The no of labs in {i} semester are:{no_of_labs1}')

    
    @classmethod
    def cse_department_details(cls):
        print(f'The department name is:{cls.branch}')
        print(f'The HOD of the department {cls.branch} is:{cls.hod_name}')

a=CSE()
print('              ')
b=ECE()


  
    
    
        
