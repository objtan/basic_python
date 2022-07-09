again = 'y'
name_list = []

while again == 'y':
    enter_name = input('Enter name: ')
    print()
    name_list.append(enter_name)

    print('Do you want to add another name?')
    again = input('y = yes, anything else = no: ')
    print()

print('danh sach ten ma ban da nhap')

for values in name_list:
    print(values)