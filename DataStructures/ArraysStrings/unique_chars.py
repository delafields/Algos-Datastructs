'''
Implement an algorithm to determine if a string has all unique characters

Contraints
    The string is ASCII
    We can assume this is case sensitive
    We can use additional data structures
    We assume this fits in memory

Test Cases
    None -> False
    '' -> True
    'foo' -> False
    'bar' -> True
'''
# Implement
class UniqueChars(object):

    def unique_chars(self, string):
        # TODO: Implement me
        pass

# Unit Test
from nose.tools import assert_equal


class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()

# Solution
class UniqueCharsSolutions(object):

    # Time: O(n), Space: Additional O(n)
    def has_unique_chars_len(self, string):
        if string is None:
            return False
        return (len(set(string)) == len(string))

    # Time: O(n), Space: Additional O(n)
    def has_unique_chars(self, string):
        if string is None:
            return False
        char_set = set()
        for char in string:
            if char in char_set:
                return False
            else:
                char_set.add(char)
        return True
