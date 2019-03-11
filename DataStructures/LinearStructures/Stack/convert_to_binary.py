from Stack import Stack

'''
Take an integer and return its binary representation
'''

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        remainder = decNumber % 2
        remstack.push(remainder)
        decNumber = decNumber // 2

    binaryString = ""
    while not remstack.isEmpty():
        binaryString += str(remstack.pop())

    return binaryString

print(divideBy2(42))

'''
Convert all Bases
'''

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        remainder = decNumber % base
        remstack.push(remainder)
        decNumber = decNumber // base

    baseString = ""
    while not remstack.isEmpty():
        baseString += digits[remstack.pop()]

    return baseString

print(baseConverter(25,2))
print(baseConverter(25,16))
