# Write a Python function to create the HTML string with tags around the word(s).

def add_tag(*arg):
    '''

    :param *arg: tag:String followed by content:String
    :return: element:String
    '''
    return f"<{arg[0]}>{arg[1]}</{arg[0]}>"


if __name__ == '__main__':
    print(add_tag('i', 'gaurav'))
    print(add_tag('b', 'gaurav'))