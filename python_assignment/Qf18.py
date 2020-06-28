# Write a Python program to check whether a given string is number or not
# using Lambda.

is_string= lambda arg: type(arg) == str


if __name__ == '__main__':
    print(is_string('gaurav'))