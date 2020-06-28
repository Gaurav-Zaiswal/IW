# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

def replace_string(arg):
    '''

    :param arg: string
    :return: string
    '''
    word_list = arg.split()
    final_str = ''
    index_of_not = word_list.index('not')
    for i in range(index_of_not):
        final_str += word_list[i]
        final_str += " "

    final_str += "good!"
    return final_str


if __name__ == '__main__':
    s = 'The lyrics is not that poor!'
    print('given string: ', s)
    print('result: ', replace_string(s))
    s1 = 'Python is not a poor language.'
    print('given string: ', s1)
    print('result: ', replace_string(s1))