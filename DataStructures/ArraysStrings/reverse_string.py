'''
Implement a function to reverse a string (a list of chars) in-place

Constraints
    We can assume the string is ASCII
    We cannot use a slice operator or the reversed function
        (as this must be in place)
    Since python strings are immutable, we use a list of characters

Test Cases
    None -> None
    [''] -> ['']
    ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']
'''
# Implement
class ReverseString:

    def reverse(self, chars):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestReverse(object):

    def test_reverse(self, func):
        assert_equal(func(None), None)
        assert_equal(func(['']), [''])
        assert_equal(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self, func):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func(target_list)
        assert_equal(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    reverse_string = ReverseString()
    test.test_reverse(reverse_string.reverse)
    test.test_reverse_inplace(reverse_string.reverse)


if __name__ == '__main__':
    main()

'''
Algorithm
    Iterate len(string)/2 times, starting with i = 0:
        Swap char with index(i) and char with index(len(string)-1-i)
        Increment i

    Complexity:
        Time: O(n)
        Space: O(1)
'''
# Solution
class ReverseStringSolution:

    def reverse(self, chars):
        if chars:
            size = len(chars)
            for i in range(size//2):
                chars[i], chars[size - 1 - i] = chars[size - 1 - i], chars[i]
            return chars

    # These are non-in-place, pythonic versions
    def reverse_string_alt(string):
        if string:
            return string[::-1]
        return string

    def reverse_string_alt2(string):
        if string:
            return ''.join(reversed(string))
        return string
