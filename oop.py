class Employee:
    num_emp=0
    raise_amount=1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last = last
        self.pay = pay
       # self.email = first + '.' + last + '@gmail.com'
        Employee.num_emp+=1
    def fullname(self):
        #return '{} {}'.format(self.first, self.last)
        return str(self.first+ ' ' + self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        return self.pay


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or  day.weekday()==6:
            return False
        return True

     # dunder Method
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return self.fullname()
    #Getter
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #Setter
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    # deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

class Developer(Employee):#Inheritance
    raise_amount = 1.10

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang= prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay,employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)


    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print('--> ' + emp.fullname())







emp_1=Employee('Md Tajul', 'Islam', 50000)
emp_2=Employee('Test', 'User', 60000)

del emp_1.fullname

#dev_1=Developer('Md Tajul', 'Islam', 50000,'Python')
#dev_2=Developer('Test', 'User', 60000,'Java')

"""
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1+emp_2)



#print(Employee.num_emp)
#print(emp_1)
#print(emp_2)



print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())
print (emp_1.pay)
print(emp_1.apply_raise())

print(dev_1.email)
print(dev_2.email)
print(dev_1.prog_lang)

import datetime
my_date= datetime.date(2019,2,12)
print(Employee.is_workday(my_date))

mng_1=Manager('Syed','Fahmi',90000,[dev_1])
print(mng_1.email)
mng_1.add_emp(dev_2)
mng_1.print_emp()
mng_1.remove_emp(dev_2)
mng_1.print_emp()
"""
