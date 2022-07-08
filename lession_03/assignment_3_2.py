# Create a variable to control the loop
keep_going = 'False'

# Create a "While" loop for the user wants to do another action
while keep_going == 'False':
    # ---------------------------------------------
    # ---------------------------------------------
    # Program code assignment 3_2
    # ---------------------------------------------]
    # ---------------------------------------------

    # Enter password
    password = input('Enter my password: ')

    # Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = True

    # Id password length >= 7 then correct_length is "True".
    if len(password) >= 7:
        correct_length = True

        # Test each character and set the appropriate flag
        # A valid password must be at least 7 characters in length, 
        # have at least one uppercase letter, one lowercase letter, and one digit, and not space.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
            if ch.isspace():
                has_space = False

    # If all conditions are satisfied then set is_valid to true and display password, opposite.
    if correct_length and has_uppercase and has_lowercase and has_digit and has_space:
        is_valid = True
        print(password)
        break

    else:
        is_valid = False
        print('Incorrect password format!!!')
        keep_going = str(is_valid)


