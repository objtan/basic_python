'''
Create a python program with 3 thread:
- Main thread for main program
- Thread 1 to display current time after one second in a loop. this thread will be end after 2 minutes.
- Thread 2 insert 1000 employees to VTI_employees database. Print notification when finishing.
- program will be ended after thread 1&2 finish their tasks.
'''
import mysql.connector
from mysql.connector import Error
import threading
import time


def display_seconds(x):
    sec = time.strftime('%S',x)
    sec = int(sec)
    print(sec)

def task1():
    for i in range(10):
        t = time.gmtime()
        display_seconds(t)
        time.sleep(1)

def Insert_multiple_records(sql, vals):
    try:
        myconn = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="vti_employees")
        if myconn.is_connected():
            cur = myconn.cursor()
            try:
                cur.executemany(sql, vals)
                myconn.commit()
                print("Insert success!, {} record(s) affected".format(cur.rowcount))
            except Error:
                print("Error: ",Error)
                myconn.rollback() 
        myconn.close()
    except Error:
        print("Error: ",Error)


def task2():
    mySql_insert_query = ("""
            INSERT INTO Employee_Info (Name, DoB, Email, MobileNumber)
            VALUES (%s, %s, %s, %s)
        """)
    vals=[]
    for i in range(10):
        # emp_id= f'{str(i)}'
        vals.append(tuple((f'tan {i} ', '2001-05-22', "tan@gmail.com", '0123456780')))

    Insert_multiple_records(mySql_insert_query, vals)
    print('Done')


def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Done all task')

main()