# Write a Python function to insert a string in the middle of a string.

def insert_string_middle(*arg):
    '''

    :param *arg: first_sting:String followed by second_string:String
    :return: element:String
    '''
    return arg[0][:len(arg[0])//2] + arg[1] + arg[0][len(arg[0])//2:]


if __name__ == '__main__':
    print(insert_string_middle('gaurav', 'APPLE'))
    print(insert_string_middle('[[]]<<>>', 'Python'))