# Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def rearrange_characters(arg):
    '''

    :param arg: word:String
    :return: word:String
    '''
    return arg[-1] + arg[1:(len(arg)-1)] + arg[0]


if __name__ == '__main__':
    print(rearrange_characters('apple'))