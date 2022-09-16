# Program make a simple calculator that can add, subtract,
# multiply and divide using functions
print('################################################')
print('Simple Calculator App')
print('################################################')

# Define functions to be used by the calculator
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Define function to obtain which function
# the user wants
def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('What would you like to do? You can:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('##############################################')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4'):
            input_ok = True
        else:
            print('Invalid input. The input (must be from 1 to 4)')
    print('################################################')
    return user_selection


def get_integer_input(message):
    """ Obtain input from user and convert to an int"""
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


def check_if_user_has_finished():
    """
    Checks that the user wants to finish or not.
    Performs some verification of the input."""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


finished = False
while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1 = get_integer_input('Input the first number: ')
    n2 = get_integer_input('Input the second number: ')
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result - multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)

    print('Result:', result)
    print('###############################')

    finished = check_if_user_has_finished()