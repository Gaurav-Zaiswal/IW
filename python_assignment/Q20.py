# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def count_string(arg):
    '''

    :param arg: list of strings
    :return: count: int
    '''

    count = 0
    for _ in arg:
        if len(_)>1 and (_[0] == _[len(_)-1]):
            count += 1
    return count


if __name__ == "__main__":
    print(count_string(['abc', 'xyz', 'aba', '1221']))