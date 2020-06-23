# Write a Python function that takes a list of words and returns the length of the
# longest one.

def longest_word(args):
    '''

    :param args: list of words
    :return:
    '''
    current_long = ''
    for i in range(len(args)):
        if i == 0:
            current_long = args[0]
        else:
            if len(args[i]) > len(current_long):
                current_long = args[i]
    return current_long


if __name__ == "__main__":
    print(longest_word(['apple', 'asdfasdf', 'adf', 'ertyuifgh', 'ty']))