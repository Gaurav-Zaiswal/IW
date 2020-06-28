# Write a Python program to print the even numbers from a given list.

def print_even_prime(arg):
    '''

    :param arg: string
    :return: list
    '''
    new_arg = []
    for _ in arg:
        if _ % 2 == 0:
            new_arg.append(_)
    return new_arg

if __name__ == "__main__":
    print(print_even_prime([1,3, 4,41, 80, 22, 10, 7]))