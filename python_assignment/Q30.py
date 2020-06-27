# Write a Python script to check whether a given key already exists in a
# dictionary.

def has_given_key(*args):
    '''

    :param args: list containing dictionary followed by a key
    :return: boolean
    '''

    return args[0].get(args[1]) is not None


if __name__ == '__main__':
    print(has_given_key({0: 10, 1: 20}, 0)) # true
    print(has_given_key({0: 10, 1: 20}, 3)) # false