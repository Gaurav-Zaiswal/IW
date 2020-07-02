# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(num):
    '''

    :param num: integer
    :return: Boolean
    '''
    if (num <= 1):
        return False

    for i in range(2, num):
        if (num % i == 0):
            return False

    return True


print(is_prime(15))