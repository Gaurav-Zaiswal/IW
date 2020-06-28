# Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

add_fifteen = lambda a: a + 15
multiply = lambda x,y: x*y


if __name__ == '__main__':
    print("Addition: ", add_fifteen(5))
    print("Multiplication: ", multiply(5, 6))