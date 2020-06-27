# Write a Python script to add a key to a dictionary.

def add_to_dict(*args):
    '''

    :param args: list whose in which key follows word
    :param kwarg: dict in which item has to be added
    :return: dict
    '''
    args[0][args[1][0]] = args[1][1]
    return args[0]


if __name__ == '__main__':
    print(add_to_dict({0: 10, 1: 20},[2, 40]))