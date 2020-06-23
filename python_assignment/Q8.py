# Write a Python program to remove the n th index character from a nonempty string.

def remove_character(*args):
    '''

    :param args: word:String followed by index:int
    :return: word:String
    '''
    return args[0][:args[1]] + args[0][args[1]+1:]


if __name__ == '__main__':
    print(remove_character('apple', 2))