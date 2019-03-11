'''
Find the single different char between two strings

Constraints
    Assume 2 strings, str1 and str2, where str2 contains the same set
        of characters as str1 plus one character
    We can assume the strings are ASCII
    All strings are lowercase
    We cannot assume the inputs are valid
    We can assume this fits in memory

Test Cases
    None input -> TypeError
    'abcd', 'abcde' -> 'e'
    'aaabbcdd', 'abdbacade' -> 'e'
'''
# Implement
class Diff(object):

    def find_diff(self, str1, str2):
        # TODO: Implement me
        pass

# Unit Test
from nose.tools import assert_equal, assert_raises


class TestFindDiff(object):

    def test_find_diff(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None, None)
        assert_equal(solution.find_diff('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()

'''
Algorithm
    Dictionary
        Keep a dict of seen values in str1
        Loop through str2, decrementing the seen values
            If the char is not there or if the decrement
            results in a negative value, return the char

        Complexity:
            Time: O(m+n) where m and n are the lengths of str1, str2
            Space: O(h), for the dict, where h is the unique chars in str1

    XOR
        XOR the two strings, which isolates the differing char

        Complexity:
            Time: O(m+n) where m and n are the lengths of str1, str2
            Space: O(1)
'''

# Solution
class DiffSolution(object):

    def find_diff_dict(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')

        seen = {}
        for char in str1:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        for char in str2:
            try:
                seen[char] -= 1
            except KeyError:
                return char
            if seen[char] < 0:
                return char
        return None

    def find_diff_xor(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')

        result = 0
        for char in str1:
            result ^= ord(char)
        for char in str2:
            result ^= ord(char)
        return chr(result)
