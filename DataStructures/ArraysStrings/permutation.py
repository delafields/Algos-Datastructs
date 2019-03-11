'''
Determine if a string is a permutation of another string

Constraints
    We can assume the string is ASCII
    Whitespace IS important
    This is case sensitive
    We CAN use additional data structures
    We assume this can fit in memory

Test Cases
    One or more None inputs -> False
    One or more empty strings -> False
    'Nib', 'bin' -> False
    'a ct', 'ca t' -> True
'''
# Implement
class Permutations:

    def is_permutation(self, str1, str2):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestPermutation(object):

    def test_permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('act', 'cat'), True)
        assert_equal(func('a ct', 'ca t'), True)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()

'''
Algorithm: Compare Sorted Strings
    Permutations contain the same strings but in different orders
    This approach could be slow for large strings due to sorting

    Sort both strings
    If both sorted strings are equal
        return True
    Else
        return False

    Complexity:
        Time: O(n log n) from the sort, in general
        Space: O(n)

Algorithm: Hash Map Lookup
    We'll keep a hash map(dict) to keep track of characters we encounter

    For each character in each string
        If the character does not exist in a hash map, add it to the hash map
        Else, increment the character's count
    If the hash maps for each string are equal
        return True
    Else
        return False
'''
# Solution
from collections import defaultdict

class PermutationsSolution:

    def is_permutation_sort(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        return sorted(str1) == sorted(str2)

    def is_permutation_hash(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False

        unique_counts1 = defaultdict(int)
        unique_counts2 = defaultdict(int)
        for char in str1:
            unique_counts1[char] += 1
        for char in str2:
            unique_counts2[char] += 1
        return unique_counts1 == unique_counts2
