'''
Implement quick sort

Constraints
    A naive solution is sufficient (ie not in-place)
    Duplicates are allowed
    Don't assume inputs are valid
    Assume it fits in memory

Test Cases
    None -> Exception
    Empty input -> []
    One element -> [element]
    Two or more elements
'''
# Implement
class QuickSort:

    def sort(self, data):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestQuickSort(object):

    def test_quick_sort(self):
        quick_sort = QuickSort()

        print('None input')
        assert_raises(TypeError, quick_sort.sort, None)

        print('Empty input')
        assert_equal(quick_sort.sort([]), [])

        print('One element')
        assert_equal(quick_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(quick_sort.sort(data), sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort()


if __name__ == '__main__':
    main()

'''
Algorithm
    Set pivot to middle element in the data
    For each element
        If the current element is the pivot
            Continue
        Elif the element is less than the pivot
            Add to left array
        Else
            Add to right array
    Recursively apply quicksort to left array
    Recursively apply quicksort to right array
    Merge the left array + pivot + right array

    Complexity:
        Time: O(n log n) average/best. O(n^2) worst
        Space: O(n)

    Notes:
        More sophisticated implementations are in-place
            although they still take up recursion depth space
        Most implementations are not stable

        Typically quicksort is significantly faster than other O(n log n)
        algorithms, because its inner loop can be efficiently implemented
        on most architectures (because it has good cache locality)
        and in most real-world data, it is possible to make design choices
        which minimize the probability of requiring quadratic Time
'''
# Solution

class QuickSortSolution:

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data
        equal = []
        left = []
        right = []
        pivot_index = len(data)//2
        pivot_value = data[pivot_index]
        # Build the left and right partitions
        for item in data:
            if item == pivot_value:
                equal.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)
        # Recursively apply quick_sort
        left_ = self._sort(left)
        right_ = self.sort(right)
        return left_ + equal + right_
