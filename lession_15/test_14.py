import mysql.connector
from mysql.connector import Error


''' 
1. Create DB
a, Create a new database named VTI_Employees.
b, Create 2 tables:
- Table 1: Employee_Info
    + Emp_ID <Primary key>
    + Name
    + DoB
    + Email
    + MobileNumber
- Table 2: Employee_Work
    + Emp_ID <fk>
    + Role
    + Department
    + Salary
2. Write the program to do following tasks:
a, Display the menu:
----------- Select Operation -------------
O_1. Display all employees information
O_2. Display employee information with specific Name
O_3. Insert a new employee
O_4. Update a specific employee with Emp_ID
O_5. Delete a specific employee with Emp_ID
b, Perform coresponding operations based on the user's choice.
'''
class Employee:

    def __init__(self, emp_id, name, dob, email, mobilenumber, role = '', department = '', salary = ''):
        self.__emp_id=emp_id
        self.__name=name
        self.__dob=dob
        self.__email=email
        self.__mobilenumber=mobilenumber
        self.__role=role
        self.__department=department
        self.__salary=salary

    def get_Employee(self):
        return tuple(self.__emp_id, self.__name, self.__dob, self.__email, self.__mobilenumber)
    
    def get_Employee_work(self):
        return tuple(self.__emp_id, self.__role, self.__department, self.__salary)
    
    def toString(self):
        return "Emp_id: {}\nName: {}\nDob: {}\nEmail: {}\nMobile number: {}\nRole: {}\nDepartment: {}\nSalary: {}\n".format(self.__emp_id, self.__name, self.__dob, self.__email, self.__mobilenumber, self.__role, self.__department, self.__salary)


class Connect:

    def __init__(self, name_database='VTI_Employees', host="localhost", user="root", passwd="root"):
        self.__con = mysql.connector.connect(host=host, database=name_database, user=user, passwd=passwd)
    
    def connect(self):
        return self.__con
    
    def close(self):
        if self.__con.is_connected():
            self.__con.close()
 

def ORM(emp):
    return Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[6], emp[7], emp[8])

def check_connect(name_database):
    try:
        conn = Connect(name_database = name_database)
        return True
    except Error:
        return False

#1. Create DB
#a Create a new database named VTI_Employees.
def Create_database(name_database, host="localhost", user="root", passwd="root"):
    try: 
        myconn = mysql.connector.connect(host=host, user=user, passwd=passwd)
        if myconn.is_connected():
            print('Connected to MySQL Database')
            cur = myconn.cursor()
            cur.execute("create database {}".format(name_database))
            print('Create database success!')
    except Error:
        print("Error: ",Error)
    finally:
        if myconn.is_connected():
            cur.close()
            myconn.close()

#b Create 2 tables:
def Create_table():
    try: 
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            excute="""
        CREATE TABLE Employee(
            Emp_ID VARCHAR(10) PRIMARY KEY,
            Name VARCHAR(50) NOT NULL,
            DoB DATETIME NULL,
            Email VARCHAR(50) NOT NULL,
            MobileNumber VARCHAR(50)  NOT NULL
        )
        CREATE TABLE Employee_work(
        Emp_ID VARCHAR(10),
        Role VARCHAR(50) NOT NULL,
        Department VARCHAR(50) NOT NULL,
        Salary int NOT NULL,
        FOREIGN KEY(Emp_ID) REFERENCES Employee(Emp_ID) ON DELETE CASCADE
        )
        """
            cur = myconn.cursor()

            cur.execute(excute)
            print('Create table success!')
        conn.close()
    except Error:
        print("Error: ",Error)


def Employee_is_exists(emp_id):
    try: 
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()
            cur.execute("SELECT * FROM Employee WHERE Emp_id = '{}'".format(emp_id))
            result = cur.fetchall()
            if result:
                return True
            else:
                return False
        conn.close()
    except Error:
        print("Error: ",Error)
   

def Insert_a_records(sql, vals):
    try:
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()
            try:
                cur.execute(sql, vals)
                myconn.commit()
                print("Insert success!, {} record(s) affected".format(cur.rowcount))
            except Error:
                print("Error: ",Error)
                myconn.rollback()
        conn.close()
    except Error:
        print("Error: ",Error)
    


def Insert_multiple_records(sql, vals):
    try:
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()
            try:
                cur.executemany(sql, vals)
                myconn.commit()
                print("Insert success!, {} record(s) affected".format(cur.rowcount))
            except Error:
                print("Error: ",Error)
                myconn.rollback() 
        conn.close()
    except Error:
        print("Error: ",Error)
        

def Show_all_employee_information():
    try: 
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()
            cur.execute("SELECT * FROM Employee as e LEFT JOIN Employee_work as w ON e.Emp_ID=w.Emp_ID")
            result = cur.fetchall() 
            if result:
                list_emp = list(map(ORM,result))
                for emp in list_emp:
                    print(emp.toString())
            else:
                print("No employee")
        conn.close()
    except Error:
        print("Error: ",Error)
        

def Show_employee_information_with_specific_name(name_emp):
    try: 
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()
            cur.execute("SELECT * FROM Employee as e LEFT JOIN Employee_work as w ON e.Emp_ID=w.Emp_ID WHERE Name = '{}'".format(name_emp))
            result = cur.fetchall()
            if result:
                list_emp = list(map(ORM,result))
                for emp in list_emp:
                    print(emp.toString())
            else:
                print("No employee")
        conn.close()
    except Error:
        print("Error: ",Error)
        

def Update_a_specific_employee_with_Emp_ID( emp_id, salary):
    try: 
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()  
            try:  
                cur.execute("UPDATE Employee_work SET Salary = {} WHERE Emp_ID = '{}'".format(salary, emp_id))
                myconn.commit()
                print(cur.rowcount, "record(s) affected")
            except Error:
                print("Error: ",Error)
                myconn.rollback()
        conn.close()
    except Error:
        print("Error: ",Error)
        

def Delete_a_specific_employee_with_Emp_ID(emp_id):
    try: 
        conn = Connect()
        myconn = conn.connect()
        if myconn.is_connected():
            cur = myconn.cursor()
            try:
                cur.execute("DELETE FROM Employee WHERE Emp_ID = '{}'".format(emp_id))
                myconn.commit()
                print(cur.rowcount, "record(s) affected")
            except Error:
                print("Error: ",Error)
                myconn.rollback()
        conn.close()
    except Error:
        print("Error: ",Error)
        

def main():
    name_database = 'VTI_Employees'
    sql_emp = ("""
            INSERT INTO Employee(Emp_ID, Name, DoB, Email, MobileNumber)
            VALUES (%s, %s, %s, %s, %s)
        """)
    sql_emp_work = ("""
            INSERT INTO Employee_work(Emp_ID, Role, Department, Salary)
            VALUES (%s, %s, %s, %s)
        """)

    if not check_connect(name_database):
        Create_database(name_database)
        Create_table(name_database)

        vals = [("PY000009", 'Dương', '2001-05-02', "duong132@gmail.com", '0123456789'),
                ("PY000014", 'Trần Hồng Vũ', '2001-09-08', "hongvu@gmail.com", '01324998')
                ]
        Insert_multiple_records(sql_emp, vals)

        vals = [("PY000009", 'Dev', 'Sale', 1200),
                ("PY000014", 'Test', 'Hanhchinh', 500)
                ]
        Insert_multiple_records(sql_emp_work, vals)

    check='y'
    while check=='y':
        print("""
        1. Display all employees information
        2. Display employee information with specific Name
        3. Insert a new employee
        4. Update a specific employee salary with Emp_ID
        5. Delete a specific employee with Emp_ID
        """)
        choose=int(input("Enter your choose: "))
        if choose == 1:
            Show_all_employee_information()

        elif choose == 2:
            name=input("Enter name: ")
            Show_employee_information_with_specific_name(name)

        elif choose == 3:
            # vals = ("PY000005", 'luan', '2001-05-22', "luanxg@gmail.com", '0123456780')
            check_switch = False
            while not check_switch:
                check_insert=input('Insert into 1.Employee / 2.Employee_work / 3.All: ')
                if check_insert == '1' or check_insert == '2' or check_insert == '3':
                    check_switch = True

            emp_id=input("Enter Employee id: ")

            if check_insert == '1':
                if not Employee_is_exists(emp_id):
                    e_name=input('Enter name of employee: ')
                    dob=input('Enter date of birth(yy-MM-dd): ')
                    email=input('Enter email: ')
                    mobilenumber=input('Enter phone number: ')
                    
                    emp=Employee(emp_id, e_name, dob, email, mobilenumber)

                    Insert_a_records(sql_emp, emp.get_Employee())

                else:
                    print("Employee id {} is exists".format(emp_id))

            elif check_insert == '2':
                if Employee_is_exists(emp_id):
                    role=input('Enter role: ')
                    department=input('Enter department: ')
                    salary=float(input('Enter salary: '))

                    Insert_a_records(sql_emp_work, tuple(emp_id, role, department, salary))
                else:
                    print("Employee id {} is not exists".format(emp_id))
            
            elif check_insert == '3':
                if not Employee_is_exists( emp_id):
                    e_name=input('Enter name of employee: ')
                    dob=input('Enter date of birth(yy-MM-dd): ')
                    email=input('Enter email: ')
                    mobilenumber=input('Enter phone number: ')
                    role=input('Enter role: ')
                    department=input('Enter department: ')
                    salary=float(input('Enter salary: '))
                    emp=Employee(emp_id, e_name, dob, email, mobilenumber, role, department, salary)

                    Insert_a_records(sql_emp, emp.get_Employee())
                    Insert_a_records(sql_emp_work, emp.get_Employee_work())
                else:
                    print("Employee id {} is exists".format(emp_id))
                    
        elif choose == 4:
            emp_id = input('Enter emp_id to update: ')
            if Employee_is_exists( emp_id):
                while True:
                    try:
                        salary=float(input('Enter new salary'))
                        break
                    except ValueError:
                        print('Enter number')
                        continue
                Update_a_specific_employee_with_Emp_ID(emp_id, salary)
            else:
                print('Emp_id {} is not exists'.format(emp_id))

        elif choose == 5:
            emp_id = input('Enter emp_id to delete: ')
            if Employee_is_exists(emp_id):
                Delete_a_specific_employee_with_Emp_ID(emp_id)
            else:
                print('Emp_id {} is not exists'.format(emp_id))
        
        check=input("Enter 'y' to continue: ").lower()

main()