# Write a Python program to remove the characters which have odd index
# values of a given string.

def remove_odd_characters(arg):
    '''

    :param arg: word:String
    :return: word:String
    '''
    return arg[::2]


if __name__ == '__main__':
    print(remove_odd_characters('apple'))