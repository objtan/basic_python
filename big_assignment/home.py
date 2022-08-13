import os
import threading

import mysql.connector
from mysql.connector import Error

import students
import subjects
import scores

# Create database function
def create_database(name_database):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='root')
        cursor = cnx.cursor()
        # =============================
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {name_database}')
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

# Create tables function
def create_tables(name_database, create_tables_query):
    cnx = None
    try:
        cnx = mysql.connector.connect(host='localhost',
                                        database=name_database,
                                        user='root',
                                        password='root')
        cursor = cnx.cursor()
        # ============================
        cursor.execute(create_tables_query)
        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

# Catch keyboard input exception function
def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice

def main():
    name_database = 'Assignment_info_manage'

    # custom ID (studen_id - PT0001) and (subject_id - SJ001)
    # do date cua file json # voi dinh dang date cua mysql nen phai de la varchar
    # sau do select DATE_FORMAT(STR_TO_DATE(DoB,'%Y-%m-%d'), '%d-%m-%Y') as DateFormat from student;
    create_tables_query = """CREATE TABLE IF NOT EXISTS custom_student_id_table (
            Custom_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY
            );
            CREATE TABLE IF NOT EXISTS custom_subject_id_table (
            Custom_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY
            );
            CREATE TABLE IF NOT EXISTS student (
            Student_ID VARCHAR(7) NOT NULL PRIMARY KEY DEFAULT '0',
            Name VARCHAR(255) NOT NULL,
            DoB DATE,
            Sex ENUM('Female', 'Male', 'Gay'),
            Address VARCHAR(255),
            Mobile_Number VARCHAR(50),
            Email VARCHAR(255)
            );
            CREATE TABLE IF NOT EXISTS subject (
            Subject_ID VARCHAR(7) NOT NULL PRIMARY KEY DEFAULT '0',
            Name VARCHAR(255) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS score (
            Student_ID VARCHAR(7) NOT NULL,
            Subject_ID VARCHAR(7) NOT NULL,
            Midel_Score FLOAT NOT NULL,
            Final_Score FLOAT NOT NULL,
            FOREIGN KEY (Student_ID) REFERENCES student(Student_ID) ON DELETE CASCADE,
            FOREIGN KEY (Subject_ID) REFERENCES subject(Subject_ID) ON DELETE CASCADE
            )"""

    # create database and table , trigger
    create_database(name_database)

    create_tables(name_database, create_tables_query)

    while True:
        os.system('cls')  # on linux / os x os.system('clear')
        print("\nChoose service you want to use : ")
        print("""
        1 : Student information management
        2 : Subject information management
        3 : Score information management
        4 : Exit"""
        )
        choice = select_in_range('Please enter a number between 1 and 4: ', 1, 4)
        if choice == 1:
            students.main() # Student information management
        if choice == 2:
            subjects.main() # Subject information management
        if choice == 3:
            scores.main() # Score information management
        if choice == 4:
            exit()
        os.system('cls')

if __name__ == "__main__":
    main()