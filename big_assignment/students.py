import os
import mysql.connector
import multimethod
import json

import home

class Student:
    def __init__(self, Name, DoB, Sex, Address, Mobile_Number, Email):
        self.Name = Name
        self.DoB = DoB
        self.Sex = Sex
        self.Address = Address
        self.Mobile_Number = Mobile_Number
        self.Email = Email

    def get_info_student(self):
        return tuple((self.Name, self.DoB, self.Sex, self.Address, self.Mobile_Number, self.Email))
        
# insert json into mysql 
def json_student_into_mysql(name_database, filename, json_student_query):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                        database=name_database,
                                        user='root',
                                        password='root')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM student')
        records = cursor.fetchall()
        if len(records) == 0:
            with open(filename, 'r') as f:
                studentsDict = json.load(f)
                studentDict = studentsDict['students']['student']
                for mykey in studentDict:
                    studentsTuple = tuple(mykey.values())
                    cursor.execute(json_student_query, studentsTuple)
        else:
            print('\nThis json file has been inserted')
        cnx.commit()
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  1. insert student function
def insert_student(name_database, insert_student_query, insert_student_records):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        cursor.execute(insert_student_query, insert_student_records)
        cnx.commit()
        print(f"{cursor.rowcount} records inserted.")
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  2. edit student function
def edit_student(name_database, select_student_id_query, param_id):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')

        cursor = cnx.cursor()
        # Student table before deleting a row"
        cursor.execute(select_student_id_query, param_id)
        records = cursor.fetchall()
        if len(records) == 0:
            print("This Student id doesn't exist")
            # display all data
            cursor.execute('SELECT * FROM student')
            # get all records
            records = cursor.fetchall()
            print("Display all data: ", cursor.rowcount)
            print("\nPrinting each row")
            for row in records:
                print(row)
        else:
            while True:
                print("""
                1 : Edit Name
                2 : Edit Birtday
                3 : Edit Sex
                4 : Edit Address
                5 : Edit Mobile Number
                6 : Edit Email
                7 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 7: ', 1, 7)
                
                # get element in tuple === print(param_id) >>> ('1',)
                param_id = param_id[0]

                if choice == 1:
                    print('-----------------')
                    Name = input('Enter new Name: ')
                    sql_update_query = ("""UPDATE student SET Name = %s WHERE Student_ID = %s""")
                    param = (Name, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 2:
                    print('-----------------')
                    DoB = input('Enter new Birthday (yy-MM-dd): ')
                    sql_update_query = ("""Update student set DoB = %s where Student_ID = %s""")
                    param = (DoB, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 3:
                    print('-----------------')
                    Sex = input('Enter new Sex (Female, Male, Gay): ').capitalize()
                    sql_update_query = ("""Update student set Sex = %s where Student_ID = %s""")
                    param = (Sex, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 4:
                    print('-----------------')
                    Address = input('Enter new Address: ')
                    sql_update_query = ("""Update student set Address = %s where Student_ID = %s""")
                    param = (Address, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 5:
                    print('-----------------')
                    Mobile_Number = input('Enter new Mobile number: ')
                    sql_update_query = ("""Update student set Mobile_Number = %s where Student_ID = %s""")
                    param = (Mobile_Number, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 6:
                    print('-----------------')
                    Email = input('Enter new Email: ')
                    sql_update_query = ("""Update student set Email = %s where Student_ID = %s""")
                    param = (Email, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 7:
                    return

        cnx.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  3. search student function
def delete_student(name_database, select_student_id_query, delete_student_id_query, param):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        # Student table before deleting a row"
        cursor.execute(select_student_id_query, param)
        records = cursor.fetchall()
        if len(records) == 0:
            print("This Student id doesn't exist")
            # display all data
            cursor.execute('SELECT * FROM student')
            print(cursor.fetchall())
        else:
            cursor.execute(delete_student_id_query, param)
            cnx.commit()
            print('number of rows deleted', cursor.rowcount)

        cnx.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  4. search student function
def search_student(name_database, select_student_query, param):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        cursor.execute(select_student_query, param)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print("\nPrinting each row")
        for row in records:
            print(row)

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def main():
    name_database = 'Assignment_info_manage'
    insert_student_query = ("""INSERT INTO student (Name, DoB, Sex, Address, Mobile_Number, Email)
            VALUES (%s, %s, %s, %s, %s, %s)""")

    delete_student_id_query = ("""DELETE FROM student WHERE Student_ID = %s""")

    select_student_id_query = ("""SELECT * FROM student WHERE Student_ID = %s """)
    select_student_name_query = ("""SELECT * FROM student WHERE Name = %s """)
    select_student_email_query = ("""SELECT * FROM student WHERE Email = %s """)

    # insert file json data into mysql
    json_student_query = ("""INSERT INTO student (Student_ID, Name, DoB, Sex, Address, Mobile_Number, Email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""")
    
  
    while True:
        print("\nChoose service you want to use : ")
        print("""
        1 : Insert Student
        2 : Edit Student
        3 : Delete Student
        4 : Search Student
        5 : Insert Data From file Json to Mysql
        6 : Go Back""")

        choice = home.select_in_range('Please enter a number between 1 and 6: ', 1, 6)
        if choice == 1:
            print('-------------------')
            print('1.insert student')
            check = 'y'
            while check == 'y':
                Name = input('Name *: ')
                DoB = input('Birthday (yy-MM-dd)*: ')              
                Sex = input('Sex (Female, Male, Gay)*: ').capitalize()
                Address = input('Adress: ').capitalize()
                Mobile_Number = input('Mobile Number: ')
                Email = input('Email: ')
                print('-----------------')
                student = Student(Name, DoB, Sex, Address, Mobile_Number, Email)
                insert_student(name_database, insert_student_query, student.get_info_student())
                print('-----------------')
                check = input("Do you want to continue(y/n): ").lower()
        elif choice == 2:
            print('-------------------')
            print('2.edit student')
            check = 'y'
            while check == 'y':
                Student_ID = input('Student ID *: ')
                print('-----------------')
                edit_student(name_database, select_student_id_query, (Student_ID,))
                print('-----------------')
                check = input("Do you want to continue edit (y/n): ").lower()
        elif choice == 3:
            print('-------------------')
            print('3.delete student')
            check = 'y'
            while check == 'y':
                Student_ID = input('Student ID *: ')
                print('-----------------')
                delete_student(name_database, select_student_id_query, delete_student_id_query, (Student_ID,))
                print('-----------------')
                check = input("Do you want to continue delete (y/n): ").lower()
        elif choice == 4:
            print('-------------------')
            while True:
                print('4.search student (ID or Name or Email)')
                print("""
                1 : Search students by ID
                2 : Search students by Name
                3 : Search students by Email
                4 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 4: ', 1, 4)
                if choice == 1:
                    Student_ID = input('Student ID *: ').upper()
                    print('-----------------')
                    search_student(name_database, select_student_id_query, (Student_ID,))
                    print('-----------------')
                if choice == 2:
                    Name = input('Name *: ')
                    print('-----------------')
                    search_student(name_database, select_student_name_query, (Name,))
                    print('-----------------')
                if choice == 3:
                    Email = input('Email: ')
                    print('-----------------')
                    search_student(name_database, select_student_email_query, (Email,))
                    print('-----------------')
                if choice == 4:
                    break
        elif choice == 5:
            print('-------------------')
            print('1.Insert Data From file Json to Mysql')
            json_student_into_mysql(name_database, 'students.json', json_student_query)
            print('-------------------')
        elif choice == 6:
            break

if __name__ == "__main__":
    main()
