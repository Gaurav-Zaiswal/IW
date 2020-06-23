# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.

def change_cases(arg):
    '''

    :param arg: word:String
    :return: List:String
    '''
    word_list = []
    word_list.append(arg.upper())
    word_list.append(arg.lower())
    return word_list


if __name__ == '__main__':
    input_word = input().strip()
    output_list = change_cases(input_word)
    for _ in output_list:
        print(_)