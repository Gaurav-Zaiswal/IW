# Write a Python program to create Fibonacci series upto n using Lambda.

sum = lambda op1, op2: op1 + op2


if __name__ == '__main__':
    n = int(input('Enter length of fibonacci: '))
    l = [0, 1, 1]
    if n>2:
        for i in range(3, n):
            l.append(sum(l[i-2], l[i-1]))

    print(l)