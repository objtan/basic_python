# 1. Define a class named Student and initialize attributes: name, age, email and sex. Create a new object of that class.
print('============================================== 1 ==============================================')
class Student:
    def __init__(self,name, age, email, sex):
        self.name = name
        self.age = age
        self.email = email
        self.sex = sex

def display_info_student(student):
    print(f'Student: {student.name} age: {student.age} email: {student.email} sex: {student.sex}')

def get_info_students():
    students = []
    check = 'y'
    while check == 'y':
        name = input('Name: ')
        age = int(input('Age: '))
        email = input('Email: ')
        sex = input('Sex: ')
        student = Student(name, age, email, sex)
        check = input("Do you want to continue(y/n): ")
        students.append(student)
    return (students)

def display_info_students(students):
    for i in range(len(students)):
        print(f'------ {i+1} ------')
        display_info_student(students[i])

def main():
    stud = get_info_students()
    display_info_students(stud)
# main()


# 2. Define a class named People with no attributes and mothods. Create a new object of that class.
print('============================================== 2 ==============================================')
class People:
    def __init__(self):
        pass

peop1 = People()

# 3. 
# 3.1 Define a class named Staff with attributes: role, department, salary and a method named show_details() to display all attributes.
# department attribute is protected, salary attribute is private.
print('============================================== 3.1 ==============================================')
class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self._department = department
        self.__salary = salary

    def get_department(self):
        return self._department

    def get_salary(self):
        return self.__salary

    def show_detail_staffs(self):
        print(f'Role: {self.role} Department: {self._department} Salary: {self.__salary} ')

staff1 = Staff('Role 1', 'Department 1','2.000.000')
staff2 = Staff('Role 2', 'Department 2','3.000.000')

staff1.show_detail_staffs()
staff2.show_detail_staffs()

# 3.2 Define a class named Student with inherited from Staff class. This class has more 2 attributes: name and age.
print('============================================== 3.2 ==============================================')
class Student3(Staff):
    def __init__(self, role, department, salary, name, age):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)

    def show_detail_students(self):
        print(f'Role: {self.role} Department: {self._department} Salary: {self.get_salary()} Name: {self.name} Age: {self.age} ')

# 3.3 Create a new object of Student then show all attributes of that object.
print('============================================== 3.3 ==============================================')
stud1 = Student3('Role 1', 'Department 1','2.000.000', 'Son', 18)
stud2 = Student3('Role 2', 'Department 2','2.000.000', 'Tan', 30)

stud1.show_detail_students()
stud2.show_detail_students()


# 4.
# 4.1 Define a class named Geometry with 2 methods: get_area() and get_perimeter().
print('============================================== 4.1 ==============================================')
class Geometry:
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

# 4.2 Define a class named Square which inherited from Geometry class. This class has 2 attributes are length and width. Override two methods from its parrent.
print('============================================== 4.2 ==============================================')
class Square(Geometry):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def get_area(self):
        S = self.length * self.width
        return S

    def get_perimeter(self):
        P = 2*(self.length + self.width)
        return P

squ = Square(3,4)
print(f'Area of Square: {squ.get_area()}')
print(f'Perimeter of Square: {squ.get_perimeter()}')

# 4.3 Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. Override 2 methods of its parrent  class.
print('============================================== 4.3 ==============================================')
class Circle(Geometry):
    def __init__(self,radius):
        self.radius = radius
        super().__init__()

    def get_area(self):
        S = self.radius * 3.14
        return S

    def get_perimeter(self):
        C = 2 * self.radius * 3.14
        return C

cir = Circle(3)
print(f'Area of Circle: {cir.get_area()}')
print(f'Perimeter of Circle: {cir.get_perimeter()}')


# 4.4 Create a new object of class Square and a new object of class Circle. Print area and primeter of those.
print('============================================== 4.4 ==============================================')