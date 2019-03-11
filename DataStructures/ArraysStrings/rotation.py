'''
Determine if a string(s1) is a rotation of another string(s2)
by calling (only once) a function is_substring

Constraints
    We can assume the string is ASCII
    This IS case sensitive
    We can use additional data structures
    We can assume this fits in memory

Test Cases
    Any strings that differ in size -> False
    None, 'foo' -> False (any None results in false)
    '', 'foo' -> False
    '', '' -> True
    'foobarbaz', -> 'barbazfoo' -> True
'''
# Implement
class Rotation:

    def is_substring(self, s1, s2):
        # TODO: Implement me
        pass

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        # Call is_substring only once
        pass

# Unit Tests
from nose.tools import assert_equal


class TestRotation(object):

    def test_rotation(self):
        rotation = Rotation()
        assert_equal(rotation.is_rotation('o', 'oo'), False)
        assert_equal(rotation.is_rotation(None, 'foo'), False)
        assert_equal(rotation.is_rotation('', 'foo'), False)
        assert_equal(rotation.is_rotation('', ''), True)
        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()

'''
Algorithm

    Complexity:
        Time: O(n)
        Space: O(n)
'''
# Solution
class RotationSolution:

    def is_substring(self, s1, s2):
        return s1 in s2

    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        return self.is_substring(s1, s2+s2)
