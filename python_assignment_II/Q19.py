# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order

# program to match opening and closing braces

def check(inp):
    stack = []
    opening = '([{'
    closing = ')]}'
    for c in inp:
        if c in opening:
            stack.append(c)
        elif c in closing:
            try:
                popped = stack.pop()
                if popped == '{' and c == '}':
                    pass
                elif popped == '(' and c == ')':
                    pass
                elif popped == '[' and c == ']':
                    pass
                else:
                    # print(popped,c)
                    return False
            except:
                # print(c)
                return False
    if len(stack) == 0:
        return True
    else:
        # print(stack)
        return False


print(check("()[]{"))
print(check('({[]{}})'))

