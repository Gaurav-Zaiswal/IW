# Write a Python program to sort a LIST OF TUPLES(not tuple) using Lambda.

sort_tuple = lambda arg: arg[0]


if __name__ == '__main__':
    l = [(2,3), (0,1), (8,3), (4, 0), (3, 2)]
    l.sort(key=sort_tuple)
    print(l)