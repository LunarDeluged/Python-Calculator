#Define the function
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

  
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))  



# Addition
        if operation == '+':
            print('{} + {} = ' .format(number_1, number_2))
            print(number_1 + number_2)

# Subtraction
        elif operation == '-':
           print('{} - {} = ' .format(number_1, number_2))
            print(number_1 - number_2)

# Multiplication
        elif operation == '*':
            print('{} * {} = ' .format(number_1, number_2))
            print(number_1 * number_2)

# Division
        elif operation == '/':
            print('{} / {} = ' .format(number_1, number_2))
            print(number_1 / number_2)

        else:
            print('You have not entered a valid operator, please run the program again.')
            calculate()


# Add again function
    again()
    
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user typs Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and the end the program
    elif calc_again.upper() == 'N':
        print('good bye you dumb donkey.')

    # If user types another key, run the function again
    else:
        again()

# Call calculate outside of function
calculate()