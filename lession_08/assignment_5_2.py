# Reads records from employee.txt file and display on screen
with open('employee.txt','rt') as fileObject:
    data = fileObject.read()
    print(data)