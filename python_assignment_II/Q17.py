# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


# First input for operands
n1, n2 = None, None
while type(n1) not in [int, float]:
    n1 = input('Enter First Number: ')
    try:
        n1 = int(n1)
    except ValueError:
        try:
            n1 = float(n1)
        except ValueError:
            print("Opps! input cannot be a String...\n")

# input for operator
operator = None
while operator not in ['+', '-', '*', '/']:
    operator = input('\nChoose the Operation: '
                     '+\t'
                     '-\t'
                     '*\t'
                     '/\t')

# second input for operands
while type(n2) not in [int, float]:
    n2 = input('\nEnter Second Number: ')
    try:
        n2 = int(n2)
    except ValueError:
        try:
            n2 = float(n2)
        except ValueError:
            print("Opps! input cannot be a String...\n")

    # handling dividing by zero exception
    if operator == '/' and n2 == 0:
        print('Opps... For division denominator has to be greater than Zero!')
        n2 = None

if operator == '+':
    print('Result:\t{} + {} = {}'.format(n1, n2, n1+n2))

if operator == '-':
    print('Result:\t{} - {} = {}'.format(n1, n2, n1-n2))

if operator == '*':
    print('Result:\t{} * {} = {}'.format(n1, n2, n1*n2))

if operator == '/':
    print('Result:\t{} / {} = {}'.format(n1, n2, n1/n2))
