# 1. Define a function that accepts 2 values and returns its sum, div, sub and multiplication (use exceptions for div)
import math
print('==================================== 1 ====================================')
def operation(a,b):
    Sum = a + b      
    Subt = a - b
    Mult = a * b
    try:
        Div = a / b
    except  ValueError:
        print("Value 2 is zero, divisision is not possible")

    return Sum,Subt,Mult,Div
# 2. Define a function to check whether a number from keyboard is a square number.
print('==================================== 2 ====================================')
# Way 1
def squar(n):
    #flag = 1 => số chính phương
    #flag = 0 => không phải số chính phương
    flag = 0
    #Tìm số bất kỳ nhỏ hơn n mà bình phương bằng n
    if (math.sqrt(n)).is_integer():
        flag = 1
    return flag
print(squar(4))
# Way 2
def is_square():
    number = int(input("Enter the Number"))

    sq_root = int(math.sqrt(number))
    return (sq_root*sq_root) == number
# 3. Define a function tha accepts 3 arguments, then check whether exist a triangle which is created by them. Return the result.
print('==================================== 3 ====================================')
def is_valid_triangle(a, b, c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# 4. Define a function that accepts one string arguments an returns number of vowels and consonants.
print('==================================== 4 ====================================')
def count_characters(word):
    vowels=0
    consonants=0
    for i in str:
        if i in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    print("The number of vowels:", vowels)
    print("\nThe number of consonant:", consonants)
# 5. Define a function that accepts a number (n) and return n first number of Fibonacci sequences.
print('==================================== 5 ====================================')
# Way 1
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))

# Way 2
def Fibonacci(n):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif n == 1:
        print("Fibonacci sequence upto", n,":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


# 6. Define a function that accepts a radius arguments an returns area and perimeter
print('==================================== 6 ====================================')
def calculate_circle(radius):
    area = radius * radius * 3.14
    perimeter = 2 * radius * 3.14
    return area, perimeter

# 7. Define a function that accepts 2 arguments: first aguments is s list of integers, second arguments is a number with default value
# 8. Repeat the list by the number, then calulate average of all items in the list
print('==================================== 7 + 8 ====================================')
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