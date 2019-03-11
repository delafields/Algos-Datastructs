from Stack import Stack

'''
Given a string of parentheses, determine whether or not they are balanced.
For example, (()))) != balanced, (((()))) == balanced
'''

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))

'''
General case for (), {}, []
'''
def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)


print(parChecker2('{{([][])}()}'))
print(parChecker2('[{()]'))

'''
Using a list
'''

def balance_check(s):

    if len(s)%2 != 0:
        return False

    opening = set('({[')
    matches = set([ ('(',')'), ('{','}'), ('[',']') ])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0

print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
