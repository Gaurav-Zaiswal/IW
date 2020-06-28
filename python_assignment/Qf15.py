# Write a Python program to filter a list of integers using Lambda.

'''
filters lists so that it has iterger > 5 only
'''
filter_list = lambda arg: arg>5


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    l1 = list(filter(filter_list, l))
    print(l1)