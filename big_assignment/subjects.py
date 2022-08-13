import os
import mysql.connector
import json

import home

class Subject:
    def __init__(self, Name):
        self.Name = Name

    def get_info_subject(self):
        return tuple((self.Name,))

# insert json into mysql 
def json_subject_into_mysql(name_database, filename, json_subject_query):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                        database=name_database,
                                        user='root',
                                        password='root')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM subject')
        records = cursor.fetchall()
        if len(records) == 0:
            with open(filename, 'r') as f:
                subjectsDict = json.load(f)
                subjectDict = subjectsDict['subjects']['subject']
                for mykey in subjectDict:
                    subjectsTuple = tuple(mykey.values())
                    cursor.execute(json_subject_query, subjectsTuple)
        else:
            print('\nThis json file has been inserted')
        
        cnx.commit()
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


#  1. insert subject function
def insert_subject(name_database, insert_subject_query, insert_subject_records):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        cursor.execute(insert_subject_query, insert_subject_records)
        cnx.commit()
        print(f"{cursor.rowcount} records inserted.")
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  2. edit subject function
def edit_subject(name_database, select_subject_id_query, param_id):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')

        cursor = cnx.cursor()
        # Student table before deleting a row"
        cursor.execute(select_subject_id_query, param_id)
        records = cursor.fetchall()
        if len(records) == 0:
            print("This subject id doesn't exist")
            # display all data
            cursor.execute('SELECT * FROM subject')
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
                2 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 2: ', 1, 2)
                
                # get element in tuple === print(param_id) >>> ('1',)
                param_id = param_id[0]

                if choice == 1:
                    print('-----------------')
                    Name = input('Enter new Name: ')
                    sql_update_query = ("""UPDATE subject SET Name = %s WHERE Subject_ID = %s""")
                    param = (Name, param_id)
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 2:
                    return

        cnx.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  3. search student function
def delete_subject(name_database, select_subject_id_query, delete_subject_id_query, param):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        # subject table before deleting a row"
        cursor.execute(select_subject_id_query, param)
        records = cursor.fetchall()
        if len(records) == 0:
            print("This subject id doesn't exist")
            # display all data
            cursor.execute('SELECT * FROM subject')
            print(cursor.fetchall())
        else:
            cursor.execute(delete_subject_id_query, param)
            cnx.commit()
            print('number of rows deleted', cursor.rowcount)

        cnx.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  4. search student function
def search_subject(name_database, select_subject_query, param):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        cursor.execute(select_subject_query, param)
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
    insert_subject_query = ("""INSERT INTO subject (Name) VALUES (%s)""")

    delete_subject_id_query = ("""DELETE FROM subject WHERE Subject_ID = %s""")

    select_subject_id_query = ("""SELECT * FROM subject WHERE Subject_ID = %s """)
    select_subject_name_query = ("""SELECT * FROM subject WHERE Name = %s """)

    # insert file json data into mysql
    json_subject_query = ("""INSERT INTO subject (Subject_ID, Name)
            VALUES (%s, %s)""")


    while True:
        print("\nChoose service you want to use : ")
        print("""
        1 : Insert Subject
        2 : Edit Subject
        3 : Delete Subject
        4 : Seach Subject
        5 : Insert Data From file Json to Mysql
        6 : Go Back"""
        )
        choice = home.select_in_range('Please enter a number between 1 and 6: ', 1, 6)
        if choice == 1:
            print('-------------------')
            print('1.insert subject')
            check = 'y'
            while check == 'y':
                Name = input('Name : ')
                subject = Subject(Name)
                insert_subject(name_database, insert_subject_query, subject.get_info_subject())
                print('-----------------')
                check = input("Do you want to continue(y/n): ").lower()
        elif choice == 2:
            print('-------------------')
            print('2.edit subject')
            check = 'y'
            while check == 'y':
                Subject_ID = input('Subject ID *: ').upper()
                print('-----------------')
                edit_subject(name_database, select_subject_id_query, (Subject_ID,))
                print('-----------------')
                check = input("Do you want to continue edit (y/n): ").lower()
        elif choice == 3:
            print('-------------------')
            print('3.delete subject')
            check = 'y'
            while check == 'y':
                Subject_ID = input('Subject ID *: ').upper()
                print('-----------------')
                delete_subject(name_database, select_subject_id_query, delete_subject_id_query, (Subject_ID,))
                print('-----------------')
                check = input("Do you want to continue delete (y/n): ").lower()
        elif choice == 4:
            print('-------------------')
            while True:
                print('4.search subject (ID or Name)')
                print("""
                1 : Search subjects by ID
                2 : Search subjects by Name
                3 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 3: ', 1, 3)
                if choice == 1:
                    Subject_ID = input('Student ID *: ').upper()
                    print('-----------------')
                    search_subject(name_database, select_subject_id_query, (Subject_ID,))
                    print('-----------------')
                if choice == 2:
                    Name = input('Name *: ')
                    print('-----------------')
                    search_subject(name_database, select_subject_name_query, (Name,))
                    print('-----------------')
                if choice == 3:
                    break
        elif choice == 5:
            print('-------------------')
            print('1.Insert Data From file Json to Mysql')
            json_subject_into_mysql(name_database, 'subjects.json', json_subject_query)
            print('-------------------')
        elif choice == 6:
            break

if __name__ == "__main__":
    main()