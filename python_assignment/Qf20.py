# Write a Python program to find intersection of two given arrays using
# Lambda.

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
l3 = list(filter(lambda x: x in l1, l2))
print (l3)


