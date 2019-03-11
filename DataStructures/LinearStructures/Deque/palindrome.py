from Deque import Deque

def palChecker(s):
    d = Deque()
    isPal = True

    for c in s:
        d.addRear(c)

    while d.size() > 1 and isPal:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            isPal = False

    return isPal

print(palChecker('radar'))
print(palChecker('ashfkjncxv'))
