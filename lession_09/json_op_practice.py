# 1. write a program to read file sample.json. Display all distance and name of locations.
import json

print('================================================ 1 =======================================')
def display_json(filename):
    with open(filename,'r') as outfile:
        obj=json.load(outfile)
        
    v1 = obj['student']
    for v2 in v1:
        print('Distance: ',v2['distance'])
        print('Name: ',v2['name'])
        print('\n')
display_json('students.json')

# 2. write a program
print('================================================ 2 =======================================')
# Define a python object (dictionary) containing fields: date,location,gps(lat,lon), wether, population.

sampleDict =[
    {
        'date': '2012',
        'location': 'ha noi',
        'gps': {
            'lat': 1222,
            'long':93939
        },
        'wether':29,
        'population':1234
    },
    {
        'date': '2012',
        'location': 'hai phong',
        'gps':  {
            'lat': 1222,
            'long':93939
        },
        'wether':24,
        'population':123477
    }
]

# store a python object (dictionary) into a json file name sample_w.json
def into_json(new_data):
    json_object = json.dumps(new_data, indent=4)
    with open("sample_w.json", "w") as outfile:
        outfile.write(json_object)
        print("into successful")
# into_json(sampleDict)

# 3. Write a program to to create a new json file from an existing json file (sample_w.json)
print('================================================ 3 =======================================')
def copy_file(filename):
    with open(filename) as outfile:
        data = json.load(outfile)

    with open('new_file.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
        print("New json file is created from sample_w.json file")
# copy_file('sample_w.json')

# 4. Write a program to add new user into existing json file (users.json). User information will be input from keyboard.

users=[
    {
        'name': 'John',
        'email': 'john@example.com',
        'age': 18,
        'address': 'John Street'
    },
    {
        'name': 'Su',
        'email': 'su@example.com',
        'age': 18,
        'address': 'Su Street'
    }
]
def add_user_from_keyboard(filename):
  
    user_list = [] 
    check='y'
    while check == 'y':
        user=dict()
        print("Enter user infor:")
        user['name']=input('Enter Name: ')
        user['email']=input('Enter Email: ')
        user['age']=int(input('Enter Age: '))
        user['address']=input('Enter Address: ')
        check = input("Do you want to continue(y/n): ")
        user_list.append(user)
    with open(filename,'w') as outfile:
        json.dump(user_list, outfile, indent=4)

# add_user_from_keyboard('users.json')


# 5. Write a program to delete users which have age is a number entered from keyboard in users.json file.
print('================================================ 5 =======================================')
def del_user_from_keyboard(filename, age):
    with open(filename,'r') as outfile:
        obj=json.load(outfile)
        for v in obj:
            if v['age']==age:
                obj.remove(v)
    with open(filename,'w') as outfile:
        json.dump(obj,outfile)

# age=int(input("Enter age which you want to delete: "))
# del_user_from_keyboard('users.json',age)

