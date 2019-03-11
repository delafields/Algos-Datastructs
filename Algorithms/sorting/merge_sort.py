'''
Implement merge sort

Constraints
    A naive solution is sufficient (ie not in-place)
    Duplicates are allowed
    Do not assume inputs are valid
    Assume this fits in memory

Test Cases
    None -> Exception
    Empty input -> []
    One element -> [element]
    Two or more elements
    Left and right subarrays of different lengths
'''
# Implement
class MergeSort:

    def sort(self, data):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestMergeSort(object):

    def test_merge_sort(self):
        merge_sort = MergeSort()

        print('None input')
        assert_raises(TypeError, merge_sort.sort, None)

        print('Empty input')
        assert_equal(merge_sort.sort([]), [])

        print('One element')
        assert_equal(merge_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(merge_sort.sort(data), sorted(data))

        print('Success: test_merge_sort')


def main():
    test = TestMergeSort()
    test.test_merge_sort()


if __name__ == '__main__':
    main()

'''
Algorithm
    Recursively split array into left and right halves
    Merge split arrays
        Using two pointers, one for each half starting at index 0
            Add the smaller element to the result array
            Increment pointer to where smaller element exists
        Copy remaining elements to the result array
        Return result array

    Complexity:
        Time: O(n log n)
        Space: O(n)

    Notes:
        Not in-place
        Most implementations are stable
        Mergesort can be good for datasets that are too large to fit in memory
            as large chunks of data can be read and written to disk
'''
# Solution

class MergeSortSolution:

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        return self._sort(data):

    def _sort(self, data):
        if len(data) < 2:
            return data
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        left = self._sort(left)
        right = self._sort(right)
        return self._merge(left, right)

    def _merge(self, left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # Copy remaining elements
        while l < len(left):
            result.append(left[l])
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1
        return result
