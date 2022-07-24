''' 1. From two lists, create a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
'''
from turtle import update
from unicodedata import name


print('==================================== 1 ====================================')
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Way 1
dict1 = dict(zip(keys,values)) # su ham zip 
print(dict1)

# Way 2

# empty dictionary
emp_dict = dict()

for i in range(len(keys)): # chay vong for tuong duong voi do dai cua chuoi keys
    emp_dict.update({keys[i]: values[i]}) # update dictionary dua vao bien i
print(emp_dict)
'''2. Frome two dictionaries, merge into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
print('==================================== 2 ====================================')
# su ding dict1 o cau 1
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Way 1
dict1.update(dict2)
print(dict1)

# Way 2
dict12 = {**dict1, **dict2} # Hop 2 tu dien (co the viet tu Python 3.5)
print(dict12)

'''3. Print the value of key 'physics' from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
'''
print('==================================== 3 ====================================')
dict3 = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
print(dict3['class']['student']['marks']['physics'])

'''4. Initialize dictionary with default values
Given:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

Expected output:
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
'''
print('==================================== 4 ====================================')
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Way 1
emp_dict4 = dict()
for i in range(len(employees)):
    emp_dict4.update({employees[i]: defaults})
print(emp_dict4)

# Way 2
res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])

'''5. Create a dictionary by extracting the keys from a given dictionary
Given:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
Keys to extract
keys = ["name", "salary"]
Expected output:
{'name': 'Kelly', 'salary': 8000}
'''
print('==================================== 5 ====================================')
dict5 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# Way 1
keys = ["name", "salary"]

newDict = {k: dict5[k] for k in keys}
print(newDict)

# way 2
# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its value from sample_dict
    res.update({k: dict5[k]})
print(res)


'''6. Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
Keys to remove
keys = ["name", "salary"]
Expected output:
{'city': 'New york', 'age': 25}
'''
print('==================================== 6 ====================================')
dict6 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Way 1
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    dict6.pop(k)
print(dict6)

# way 2
# Keys to remove
keys = ["name", "salary"]

dict6 = {k: dict6[k] for k in dict6.keys() - keys}
print(dict6)

'''7. Check if value 200 exists in the following dictionary.
Given:
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
200 present in a dict
'''
print('==================================== 7 ====================================')
#sample_dict7 = dict(a = 100, b = 200, c = 300)
dict7 = {'a': 100, 'b': 200, 'c': 300}

# Way 1
dict7.values()
if 200 in dict7.values():
    print("200 present in a dict")

# Way 2
for key, value in dict7.items():
    if value == 200:
        print(f"{value} present in a dict")

'''8. Rename a key city to a location in the following dictionary
Given:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''
print('==================================== 8 ====================================')
dict8 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

dict8['location'] = dict8.pop('city')
print(dict8)

'''9. Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
'''
print('==================================== 9 ====================================')
dict9 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# Way 1
key_min = min(dict9.keys(), key=(lambda k: dict9[k]))
print('key of min value: ',key_min)
# Way 2
key_max = max(dict9, key=dict9.get)
print('key of max value: ',key_max)


'''10. Change Brad’s salary to 8500 in the following dictionary.
Given:
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
Expected output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
'''
print('==================================== 10 ====================================')
dict10 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
# Way 1
# dict10['emp3']['salary'] = 8500
# print(dict10)
# # Way 2
for k1,v1 in dict10.items():
    for k2,v2 in v1.items():
        # if v2 == 'Brad':
            print(f'{k2}{v2}')
            # v2[k2] = 8500
            # print(dict10)
