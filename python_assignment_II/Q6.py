# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

friend_list = ['Ram', 'Jesus', 'Allah', 'Budha']

print('List of names:\n', friend_list)
print('Searching for John...')
flag = 0
for name in friend_list:
    if name == 'John':
        flag = 1
        break

if flag == 0:
    print('John not found!')
