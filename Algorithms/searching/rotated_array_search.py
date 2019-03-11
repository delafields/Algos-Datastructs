'''
Find an element in a sorted array that has been rotated a number of times

Constraints
    The input is an array of ints
    We do not know how many times the array was rotated
    The array was originally sorted in increasing order
    For the output, we return the index
    Do not assume the inputs are valid
    Assume this fits in memory

Test Cases
    None -> Exception
    [] -> None
    Not found -> None
    General case with duplicates
    General case without duplicates
'''
# Implement

class Array:

    def search_sorted_array(self, array, val):
        # TODO: implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestArray(object):

    def test_search_sorted_array(self):
        array = Array()
        assert_raises(TypeError, array.search_sorted_array, None)
        assert_equal(array.search_sorted_array([3, 1, 2], 0), None)
        assert_equal(array.search_sorted_array([3, 1, 2], 0), None)
        data = [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
        assert_equal(array.search_sorted_array(data, val=1), 3)
        data = [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]
        assert_equal(array.search_sorted_array(data, val=2), 2)
        print('Success: test_search_sorted_array')


def main():
    test = TestArray()
    test.test_search_sorted_array()


if __name__ == '__main__':
    main()

'''
Algorithms

    General case without duplicates
        index                   0   1   2   3   4   5   6   7   8   9
        input                 [ 1,  3,  5,  6,  7,  8,  9, 10, 12, 14]
        input rotated 1x      [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
        input rotated 2x      [ 5,  6,  7,  8,  9, 10, 12, 14,  1,  3]
        input rotated 3x      [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]

        find 1
        len = 10
        mid = 10 // 2 = 5
                                s                   m               e
        index                   0   1   2   3   4   5   6   7   8   9
        input                 [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]

        input[start] > input[mid]: Left half is rotated
        input[end] >= input[mid]: Right half is sorted
        1 is not within input[mid+1] to input[end] on the right side, go left

                                s       m       e
        index                   0   1   2   3   4   5   6   7   8   9
        input                 [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]

        input[start] <= input[mid]: Right half is rotated
        input[end] >= input[mid]: Left half is sorted
        1 is not within input[left] to input[mid-1] on the left side, go right

    General case with dupes
                                s                   m               e
        index                   0   1   2   3   4   5   6   7   8   9
        input                 [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  2]

        input[start] == input[mid], input[mid] != input[end], go right

        input rotated 1x      [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]

        input[start] == input[mid] == input[end], search both sides

        Complexity:
            Time: O(log n) if there are no duplicates, else O(n)
            Space: O(m), where m is the recursion depth
'''
# Solution

class ArraySolution:

    def search_sorted_array(self, array, val):
        if array is None or val is None:
            raise TypeError('array or val cannot be None')
        if not array:
            return None
        return self._search_sorted_array(array, val, start=0, end=len(array) - 1)

    def _search_sorted_array(self, array, val, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        if array[mid] == val:
            return mid
        # Left side is sorted
        if array[start] < array[mid]:
            if array[start] <= val < array[mid]:
                return self._search_sorted_array(array, val, start, mid - 1)
            else:
                return self._search_sorted_array(array, val, mid + 1, end)
        # Right side is sorted
        elif array[start] > array[mid]:
            if array[mid] < val <= array[end]:
                return self._search_sorted_array(array, val, mid + 1, end)
            else:
                return self._search_sorted_array(array, val, start, mid - 1)
        # Duplicates
        else:
            if array[mid] != array[end]:
                return self._search_sorted_array(array, val, mid + 1, end)
            else:
                result = self._search_sorted_array(array, val, start, mid - 1)
                if result != None:
                    return result
                else:
                    return self._search_sorted_array(array, val, mid + 1, end)
