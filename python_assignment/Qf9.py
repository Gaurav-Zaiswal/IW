# Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def is_prime(arg):
    '''

    :param arg: string
    :return: list
    '''
    for i in range(2, arg-1):
        if arg % i != 0:
            return True
    return False

if __name__ == "__main__":
    print(is_prime(7))