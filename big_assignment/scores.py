import collections
from hashlib import new
import os
import mysql.connector
import json

import home

class Score:
    def __init__(self, Student_ID, Subject_ID, Midel_Score, Final_Score):
        self.Student_ID = Student_ID
        self.Subject_ID = Subject_ID
        self.Midel_Score = Midel_Score
        self.Final_Score = Final_Score

    def get_info_score(self):
        return tuple((self.Student_ID, self.Subject_ID, self.Midel_Score, self.Final_Score))


# insert json into mysql 
def json_score_into_mysql(name_database, filename, json_score_query):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                        database=name_database,
                                        user='root',
                                        password='root')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM score')
        records = cursor.fetchall()
        if len(records) == 0:
            with open(filename, 'r') as f:
                scoresDict = json.load(f)
                scoreDict = scoresDict['scores']['score']
                for mykey in scoreDict:
                    scoresTuple = tuple(mykey.values())
                    cursor.execute(json_score_query, scoresTuple)
        else:
            print('\nThis json file has been inserted')

        cnx.commit()
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

#  1. insert score function
def insert_score(name_database, insert_score_query, select_score_query, insert_score_records):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
    
        cursor = cnx.cursor()
        # get studen id and subject id from the keyboard
        param = (insert_score_records[0], insert_score_records[1])
        cursor.execute(select_score_query, param)
        records = cursor.fetchall()
        if len(records) == 0:
            cursor.execute(insert_score_query, insert_score_records)
            cnx.commit()
            print(f"{cursor.rowcount} records inserted.")
            cursor.close()
        else:
            print("\nSubject id and subject id exist")
    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


#  2. edit score function
def edit_score(name_database, select_score_query, insert_score_records):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')

        cursor = cnx.cursor()
        cursor.execute(select_score_query, insert_score_records)
        records = cursor.fetchall()
        if len(records) == 0:
            print("This Student id doesn't exist \n")
            # display all data
            cursor.execute('SELECT * FROM score')
            # get all records
            records = cursor.fetchall()
            print("Display all data: ", cursor.rowcount)
            print("\nPrinting each row")
            for row in records:
                print(row)
        else:
            while True:
                print("""
                1 : Edit Midel Score
                2 : Edit Final Score
                3 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 3: ', 1, 3)

                if choice == 1:
                    print('-----------------')
                    Midel_Score = float(input('Midel Score: '))
                    sql_update_query = ("""UPDATE score SET Midel_Score = %s WHERE Student_ID = %s and Subject_ID = %s""")
                    param = (Midel_Score, insert_score_records[0], insert_score_records[1])
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 2:
                    print('-----------------')
                    Final_Score = float(input('Final Score: '))
                    sql_update_query = ("""UPDATE score SET Final_Score = %s WHERE Student_ID = %s and Subject_ID = %s""")
                    param = (Final_Score, insert_score_records[0], insert_score_records[1])
                    cursor.execute(sql_update_query, param)
                    cnx.commit()
                    print("Record Updated successfully ")
                    print('-----------------')
                if choice == 3:
                    return

        cnx.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


#  3. search student function
def search_score(name_database, select_score_query, param):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
        cursor = cnx.cursor()
        print(param)
        cursor.execute(select_score_query, param)
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

# 4. statistics score function
def statistics_score(name_database, select_score_studgrade_query, param):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
    
        cursor = cnx.cursor()
        cursor.execute(select_score_studgrade_query, param)
        records = cursor.fetchall()
        print("Display all data: ", cursor.rowcount)
        print(f"Students get an {param[0]}\n")
        for row in records:
            print(row)
        

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

# Export Data From Mysql To json file
def export_data_json(name_database, export_json_query):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                    database=name_database,
                                    user='root',
                                    password='root')
    
        cursor = cnx.cursor()
        cursor.execute(export_json_query)
        records = cursor.fetchall()
        objects_list = []
        for row in records:
            d = collections.OrderedDict()
            d["Student_ID"] = row[0]
            d["Name"] = row[1]
            d["Sex"] = row[2]
            d["Address"] = row[3]
            d["Mobile_Number"] = row[4]
            d["Email"] = row[5]
            d["Name"] = row[6]
            d["Midel_Score"] = row[7]
            d["Final_Score"] = row[8]
            d["Per_Marks"] = row[9]
            d["Grade"] = row[10]
            objects_list.append(d)
        j = json.dumps(objects_list)
        with open("export_data.json", "w") as f:
            f.write(j)

        print('Export successfully')

        cnx.close()
                

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def main():
    name_database = 'Assignment_info_manage'
    insert_score_query = ("""INSERT INTO score (Student_ID, Subject_ID, Midel_Score, Final_Score)
            VALUES (%s, %s, %s, %s)""")


    select_score_query = ("""select * from score where Student_ID = %s and Subject_ID = %s""")
    select_score_studid_query = ("""SELECT stu.Name, sco.Student_ID, sco.Midel_Score, sco.Final_Score FROM score sco 
                            INNER JOIN student stu 
                            ON sco.Student_ID = stu.Student_ID 
                            WHERE stu.Student_ID = %s """)
    select_score_studname_query = ("""SELECT stu.Name, sco.Student_ID, sco.Midel_Score, sco.Final_Score FROM score sco 
                            INNER JOIN student stu 
                            ON sco.Student_ID = stu.Student_ID 
                            WHERE stu.Name = %s """)

    select_score_studgrade_query = ("""SELECT stu.Name, sco.Student_ID, sco.Midel_Score, sco.Final_Score FROM score sco 
                            INNER JOIN student stu 
                            ON sco.Student_ID = stu.Student_ID 
                            WHERE sco.Grade = %s """)

    export_json_query = ("""SELECT stu.Student_ID, stu.Name, stu.Sex, stu.Address, stu.Mobile_Number,
                            stu.Email, sub.Name, sco.Midel_Score, sco.Final_Score, sco.Per_Marks, sco.Grade
                            FROM student stu 
                            INNER JOIN score sco 
                            ON stu.Student_ID = sco.Student_ID 
                            INNER JOIN subject sub
                            ON sco.Subject_ID = sub.Subject_ID
                            """)

    # insert file json data into mysql
    json_score_query = ("""INSERT INTO score (Student_ID, Subject_ID, Midel_Score, Final_Score)
            VALUES (%s, %s, %s, %s)""")

    while True:
        print("\nChoose service you want to use : ")
        print("""
        1 : Insert Data From file Json to Mysql
        2 : Insert Score
        3 : Edit Score
        4 : Seach Score
        5 : Statistic Score
        6 : Export Data From Mysql To json file
        7 : Back Home"""
        )
        choice = home.select_in_range('Please enter a number between 1 and 7: ', 1, 7)
        if choice == 1:
            print('-------------------')
            print('1.Insert Data From file Json to Mysql')
            json_score_into_mysql(name_database, 'scores.json', json_score_query)
            print('-------------------')
        elif choice == 2:
            print('-------------------')
            print('2.insert score')
            check = 'y'
            while check == 'y':
                Student_ID = input('Student ID : ').upper()
                Subject_ID = input('Subject ID: ').upper()           
                Midel_Score = float(input('Midel Score: '))
                Final_Score = float(input('Final Score: '))
                print('-----------------')
                score = Score(Student_ID, Subject_ID, Midel_Score, Final_Score)
                insert_score(name_database, insert_score_query, select_score_query, score.get_info_score())
                print('-----------------')
                check = input("Do you want to continue(y/n): ").lower()
        elif choice == 3:
            print('-------------------')
            print('3.Edit score')
            check = 'y'
            while check == 'y':
                Student_ID = input('Student ID : ').upper()
                Subject_ID = input('Subject ID: ').upper()           
                new_tuple = tuple((Student_ID, Subject_ID))
                print('-----------------')
                edit_score(name_database, select_score_query, new_tuple)
                print('-----------------')
                check = input("Do you want to continue(y/n): ").lower()
        elif choice == 4:
            print('-------------------')
            while True:
                print('4.search score (student id or student name)')
                print("""
                1 : Search score by student id
                2 : Search score by student name
                3 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 3: ', 1, 3)
                if choice == 1:
                    Student_ID = input('Student ID: ').upper()
                    print('-----------------')
                    search_score(name_database, select_score_studid_query, (Student_ID,))
                    print('-----------------')
                if choice == 2:
                    Name = input('Name: ')
                    print('-----------------')
                    search_score(name_database, select_score_studname_query, (Name,))
                    print('-----------------')
                if choice == 3:
                    return
        elif choice == 5:  
            while True:
                print('5. Statistics score')
                print("""
                1 : List students - A
                2 : List students - B
                3 : List students - C
                4 : List students - D
                5 : List students - F
                6 : Go Back""")

                choice = home.select_in_range('Please enter a number between 1 and 6: ', 1, 6)
                if choice == 1:
                    print('-----------------')
                    param = ('A',)
                    statistics_score(name_database, select_score_studgrade_query, param)
                    print('-----------------')
                if choice == 2:
                    print('-----------------')
                    param = ('B',)
                    statistics_score(name_database, select_score_studgrade_query, param)
                    print('-----------------')
                if choice == 3:
                    print('-----------------')
                    param = ('C',)
                    statistics_score(name_database, select_score_studgrade_query, param)
                    print('-----------------')
                if choice == 4:
                    print('-----------------')
                    param = ('D',)
                    statistics_score(name_database, select_score_studgrade_query, param)
                    print('-----------------')
                if choice == 5:
                    print('-----------------')
                    param = ('F',)
                    statistics_score(name_database, select_score_studgrade_query, param)
                    print('-----------------')
                if choice == 6:
                    break  
        elif choice == 6:
            print('-------------------')
            print('6.Export Data From Mysql To json file')
            export_data_json(name_database, export_json_query)
        elif choice == 7:
            break

if __name__ == "__main__":
    main()
