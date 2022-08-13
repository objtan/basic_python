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
    + Name <Secondary key>
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

import mysql.connector

myconn = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root",
                                database="vti_employees")

cur = myconn.cursor()

# Create database
# cur.execute("CREATE DATABASE VTI_Employees")

'''
b, Create 2 tables:
- Table 1: Employee_Info
    + Emp_ID <Primary key>
    + Name
    + DoB
    + Email
    + MobileNumber
'''
# cur.execute("DROP TABLE IF EXISTS Employee_Info")
# cur.execute("CREATE TABLE Employee_Info (Emp_ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, DoB DATETIME, Email VARCHAR(100) NOT NULL, MobileNumber VARCHAR(20) NOT NULL)")

'''
- Table 2: Employee_Work
    + Emp_ID <Secondary key>
    + Role
    + Department
    + Salary
'''
# cur.execute("DROP TABLE IF EXISTS Employee_Work")
# cur.execute("CREATE TABLE Employee_Work(Emp_ID VARCHAR(50) NOT NULL, Role VARCHAR(255) NOT NULL, Department VARCHAR(255) NOT NULL, Salary VARCHAR(255) NOT NULL)")
# , FOREIGN KEY (Emp_ID) REFERENCES Employee_Info(Emp_ID)")

# O_1. Display all employees information
'''sql_select_Query = "select * from Employee_Info"
cur = myconn.cursor()
cur.execute(sql_select_Query)
# get all records
records = cur.fetchall()
print("Total number of rows in table: ", cur.rowcount)

print("\nPrinting each row")
for row in records:
    print("Emp_ID = ", row[0], )
    print("Name = ", row[1])
    print("DoB  = ", row[2])
    print("Email  = ", row[3])
    print("MobileNumber  = ", row[4], "\n")'''

'''sql_select_Query = "select * from Employee_Work"
cur = myconn.cursor()
cur.execute(sql_select_Query)
# get all records
records = cur.fetchall()
print("Total number of rows in table: ", cur.rowcount)

print("\nPrinting each row")
for row in records:
    print("Emp_ID = ", row[0], )
    print("Role = ", row[1])
    print("Department  = ", row[2])
    print("Salary  = ", row[3], "\n")'''

# O_2. Display employee information with specific Name
'''sql_select_Query = ("SELECT * FROM Employee_Info a INNER JOIN Employee_Work d ON a.Emp_ID = d.Emp_ID WHERE a.Name = 'Nguyen Van Tan'")

cur.execute(sql_select_Query)

myresult = cur.fetchall()

for x in myresult:
  print(x)'''

#  O_3. Insert a new employee
'''sql_select_Query = "INSERT INTO Employee_Info (Name, DoB, Email, MobileNumber) VALUES (%s, %s, %s, %s)"
val = ("John Smith", "1999-05-11", "John@gmail.com", "+817777777777")
cur.execute(sql_select_Query, val)

myconn.commit()

print(cur.rowcount, "record inserted.")'''

# O_4. Update a specific employee with Name
'''sql_select_Query = "UPDATE Employee_Info SET Name = 'Nguyen Van A' WHERE Name = 'Nguyen Van Tan'"

cur.execute(sql_select_Query)

myconn.commit()

print(cur.rowcount, "record(s) affected")'''

# O_5. Delete a specific employee with Name
'''sql = "DELETE FROM Employee_Info WHERE Name = 'John Smith'"

cur.execute(sql)

myconn.commit()

print(cur.rowcount, "record(s) deleted")'''