'''
Write a Python program to calculate the payroll of employees in a company.
There are 2 types of employees: full-time and part-time employees
Need to have classes:

1. Employee: abstract class
- 2 atributes: firt name and last name
- 1 method to return full name
- 1 abstract method to return salary for employees

2. Full-time employee: inherited from employee class
- 1 atributes: salary.

3. Part-time employee: inherited from employee class
- 2 atributes: worked_hours and rate

4. Payroll: 
- 1 atribute: employee list
- 1 method to append employee to employee list
- 1 more method to show full name and salary for a given employee.

The program will receive employee information from the keyboard.

'''
from abc import ABC, abstractmethod
from contextlib import nullcontext

class Employee(ABC):
    def __init__(self, firt_name, last_name):
        self.firt_name = firt_name
        self.last_name = last_name

    def get_full_name(self):
        return self.firt_name +' '+ self.last_name

    @abstractmethod
    def get_salary(self):
        pass


class Fulltimeemppoyee(Employee):
    def __init__(self, first_name, last_name, salary):
        self.salary = salary
        super().__init__(first_name, last_name)

    def get_salary(self):
        return self.salary


class Parttimeemployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        self.worked_hours = worked_hours
        self.rate = rate
        super().__init__(first_name, last_name)

    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:
    def __init__(self):
         self.employees = []

    def append_employee(self, employee):
        self.employees.append(employee)
        # return self.employees
            
    def display_employees(self):
        for employee in self.employees:    
            print(f'Full Name : {employee.get_full_name()} ')
            print(f'Sarary - Full Time: {employee.get_salary()} VND')
            print('-------------------')


def main():
    obj_pay_roll = Payroll()
    print('------------------------ -------------------- ------------------------')
    print('------------------------ Enter list employees ------------------------')
    # append employee
    check = 'y'
    while check == 'y':
        print('Full Time is "f" or "f"----Part Time is "P" or "p"')
        check_full_part_time_empl = input()
        if check_full_part_time_empl.lower() == 'f':
            first_name = input('Firt Name: ')
            last_name = input('Last Name: ')
            salary = '20000000'
            full_time_empl = Fulltimeemppoyee(first_name, last_name, salary)
            obj_pay_roll.append_employee(full_time_empl)
        elif check_full_part_time_empl.lower() == 'p':
            first_name = input('Firt Name: ')
            last_name = input('Last Name: ')
            worked_hours = int(input('Worked Hours: '))
            rate = 200000
            part_time_empl = Parttimeemployee(first_name, last_name, worked_hours, rate)
            obj_pay_roll.append_employee(part_time_empl)
        else:
            print('you must enter F,f or P,p')
        check = input("Do you want to continue(y/n): ")
        print()

    print('------------------------ -------------------- ------------------------')
    print('------------------------ Display list employees ------------------------')
    # Display employees
    obj_pay_roll.display_employees()

main()
        
        
