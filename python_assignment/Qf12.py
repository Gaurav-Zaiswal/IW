# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def multiply(arg):
    t = int(input('enter any number'))
    return t*arg


if __name__ == '__main__':
    print(multiply(9))