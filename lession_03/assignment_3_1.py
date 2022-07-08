# Create a variable to control the loop
keep_going = 'y'

# Create a "While" loop for the user wants to do another action
while keep_going == 'y':
    # ---------------------------------------------
    # ---------------------------------------------
    # Program code assignment 2_1
    # ---------------------------------------------]
    # ---------------------------------------------
    # Create a variable start with 0
    count = 0

    # Enter a string
    my_string = input('Enter s string: ')
    
    # Convert the string you just entered to lowercase
    my_string_lower = (my_string.lower())

    # Use loop to count
    for substring in my_string_lower:
        if substring == 't':   # If not convert the string (line 18,19) then use code " if substring == 'T' or substring =='t'"
            count += 1
    print (f'Number of times the letter "T" or "t" appears in the string: {count}')


    #print(my_string_lower)

    # See if the user wants to do another action
    keep_going = input('Do you want to perform another action? (Enter y for yes): ')
