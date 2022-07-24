from datetime import date, datetime


def save_emp_record(filename,num_emps):
    with open(filename, 'a') as emp_file:
        for count in range(1, num_emps + 1):
            #Get the data for an employee.
            print(f'Enter data for employee #{count}')
            name = input('Name: ')
            id_num = input('ID number: ')
            dept = input('Department: ')
            print()

            # Write the data as a record to the file.
            emp_file.write(f'{name}\n')
            emp_file.write(f'{id_num}\n')
            emp_file.write(f'{dept}\n')
            print()

# num_emps = int(input('How many employee records do you want to create? '))
# save_emp_record('employee.txt',num_emps)
'''============================================================'''
# creating the date object of today's date
todays_date = date.today()
now = datetime.today()
  
# printing now date
print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)