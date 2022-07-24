# 8. Repeat the list by the number, then calulate average of all items in the list
# Create function list_number
# def list_number(new_list):
#     new_list = []
#     again = 'y'
#     while again == 'y':
#         enter_number = float(input('Enter a number: '))
#         new_list.append(enter_number)
#         print('Do you want to add another number?')
#         again = input('y = yes, press any key to complete the list: ')
#         print()


# Create Function average list

def main():
# Create list_number
    print('===========================Create List===========================')
    new_list = []
    again = 'y'
    while again == 'y':
        
        try:
            enter_number = float(input('Enter a number: '))
            new_list.append(enter_number)          
        except: print('alphanumeric characters cannot be entered')
        print('Do you want to add another number?')
        again = input('y = yes, press any key to complete the list: ')
        print()
    print('My list number: ',new_list)
    # calculate average of number list
    try:
        sum = 0
        for i in new_list:
            sum += i
        ave = sum/len(new_list)
        print('calculate average of number list',ave)
    except ZeroDivisionError as e: 
        print('ZeroDivisionError',e)
    print()


# Call the main function.
if __name__ == '__main__':
    main()