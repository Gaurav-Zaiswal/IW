# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

def join_strings(*args):
    return args[1][:2] + args[0][2:] + ' ' + args[0][:2] + args[1][2:]


if __name__ == "__main__":
    print(join_strings('apple', 'asdf'))
    print(join_strings('abc', 'xyz'))