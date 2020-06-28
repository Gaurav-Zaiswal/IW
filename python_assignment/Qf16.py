# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

square = lambda arg: arg*arg
cube = lambda arg: arg*arg*arg


if __name__ == '__main__':
    l = [1,2,8,9,10]
    for _ in l:
        print('number: ', _)
        print('square: ', square(_))
        print('cube: ', cube(_))