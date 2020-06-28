# Write a Python program to print the even numbers from a given list.

def print_even_prime(arg):
    '''

    :param arg: string
    :return: list
    '''
    new_arg = []
    for i in range(0, len(arg), 2):
        new_arg.append(arg[i])
    return new_arg

if __name__ == "__main__":
    print(print_even_prime([1,2,3,4,5,6]))