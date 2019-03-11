'''
Sort an array of strings so all anagrams are next to eachother

Constraints
    There are no sorting requirements other than the grouping of anagrams
    Don't assume inputs are valid
    Assume it fits in memory

Test Cases
    None -> Exception
    [] -> []
    General Case:
        Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
'''
# Implement

from collections import OrderedDict


class Anagram:

    def group_anagrams(self, items):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestAnagrams(object):

    def test_group_anagrams(self):
        anagram = Anagram()
        assert_raises(TypeError, anagram.group_anagrams, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        assert_equal(anagram.group_anagrams(data), expected)

        print('Success: test_group_anagrams')


def main():
    test = TestAnagrams()
    test.test_group_anagrams()


if __name__ == '__main__':
    main()

'''
Algorithm
    Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']

    Sort the chars for each item:
        'ram' -> 'amr'
        'act' -> 'act'
        'arm' -> 'amr'
        'abt' -> 'bat'
        'cat' -> 'act'
        'abt' -> 'tab'

    Use a map of sorted chars to each item to group anagrams:
        {
            'amr': ['ram', 'arm'],
            'act': ['act', 'cat'],
            'abt': ['bat', 'tab']
        }

    Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']

    Complexity:
        Time: O(k * n), due to the modified bucket sort
        Space: O(n)
'''

from collections import OrderedDict

class AnagramSolution:

    def group_anagrams(self, items):
        if items is None:
            raise TypeError('items cannot be None')
        if not items:
            return items

        anagram_map = OrderedDict()
        for item in items:
            # Use a tuple, which is hashable and
            # serves as the key in anagram_map
            sorted_chars = tuple(sorted(item))
            if sorted_chars in anagram_map:
                anagram_map[sorted_chars].append(item)
            else:
                anagram_map[shorted_chars] = item
        result = []
        for value in anagram_map.values():
            result.extend(value)
        return result
