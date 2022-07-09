# 1. Create a list my_list with item which have different data types and length at least 5
from itertools import count
from operator import index
from re import A
print('============================================')
my_list = [5,7,'Python',8,'Java',1]

# 2. Print all items of my_list in single line
print('============================================')
for ch in my_list:
    print(ch)

# 3. Count the number of each items in my_list --------
print('============================================')
for values in my_list:
    # print ("number of items in the list : ", my_list.count(index))
    print("count the number of {} in my_list is: {}".format(values,my_list.count(values)))
print('============================================')
for i,v in enumerate(my_list):
    # print ("number of items in the list : ", my_list.count(index))
    print("count the number of {} in my_list is: {}".format(v,my_list.count(v)))
# 4. Reverse the order of the items in my_list
print('============================================')
my_list.reverse()
print(my_list)

# 5. Square the numeric items of items in my_list then print result
print('============================================')
for values in my_list:
    if type(values) is int or type(values) is float:
        values = values ** 2      
    print(values)

# 6. Add some single values an iterable values to my_list
print('============================================')
my_list.append('Tan')
print(my_list)
my_list.extend(['Hello',5])
print(my_list)

# 7. Remove values at the end and at the second position of my_list
print('============================================')
# my_list.pop(2)
# my_list.pop()
# print(my_list)
# 8. Display those items from my_list that are deivisible by 5 ---------------
print('============================================')
for values in my_list:
    if type(values) is int:
        if values % 5 == 0:
            print(f'intem divisible by 5 is: {values}')

# 9. Calculate the sum of all numeric items in my_list
print('============================================')
sum = 0
for values in my_list:
    if type(values) is int or type(values) is float:
        sum += values
print(f'sum of list = {sum}')

# 10. Create a new list named my_list_str from all string items in my_list, then uppercase them
print('============================================')
my_list_str = []
for values in my_list:
    if type(values) is str:
        my_list_str.append(values.upper())
print(my_list_str)

# 11. Create a new list my_list_num from all string items in my_list, then sort them
print('============================================')
my_list_num = []
for values in my_list:
    if type(values) is int or type(values) is float:
        my_list_num.append(values)
my_list_num.sort()
print(my_list_num)

# 12. Find maximum/nimimum values of my_list_num
print('============================================')
max = max(my_list_num)
print(f'the largest number is {max}')

min = min(my_list_num)
print(f'the smallest number is {min}')

print('============================================')
max=my_list_num[0] # gan gia tri max cho vi tri dau tien
min=my_list_num[0] # gan gia tri min cho vi tri dau tien
for i in range(1,len(my_list_num)): # Ham range ta lay vi tri sau vi tri max duoc gan (vi tri thu 2) cho den het danh sach
    if my_list_num[i]>max: # vi tri thu 2 ma lon hon max duoc gan ban dau thi lay gia thu 2, cu vay so sanh den het chuoi
        max=my_list_num[i]
    if my_list_num[i]<min:
        min=my_list_num[i]
print("max in my_list_num: ",max)
print("min in my_list_num: ",min)

# 13. Remove duplicate values from my_list_num, if have
print('============================================')
new_list = []
for values in my_list_num:
    if values not in new_list:
        new_list.append(values)
print(new_list)

# 14. Display old and even number of my_list_num
print('============================================')
list_num_old = []
list_num_even = []
for values in my_list_num:
    if values % 2 == 0:
        list_num_old.append(values)
    else:
        list_num_even.append(values)
print(list_num_old)
print(list_num_even)


