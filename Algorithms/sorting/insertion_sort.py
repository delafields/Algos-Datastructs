'''
Implement insertion sort

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

class InsertionSort:

    def sort(data):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestInsertionSort(object):

    def test_insertion_sort(self):
        insertion_sort = InsertionSort()

        print('None input')
        assert_raises(TypeError, insertion_sort.sort, None)

        print('Empty input')
        assert_equal(insertion_sort.sort([]), [])

        print('One element')
        assert_equal(insertion_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(insertion_sort.sort(data), sorted(data))

        print('Success: test_insertion_sort')


def main():
    test = TestInsertionSort()
    test.test_insertion_sort()


if __name__ == '__main__':
    main()

'''
Algorithm
    For each value index 1 to n-1
        Compare with all elements to the left of the current value to determine new insertion point
            Hold current value in temp variable
            Shift elements from new insertion point right
            Insert value in temp variable
            Break

    Complexity:
        O(n^2) average/worst. O(1) best if input is already sorted
        Space: O(1) for the iterative solution

    Notes:
        In-place
        Stable
        Insertion sort works well for very small datasets where most of the input is already sorted
'''
# Solution

class InsertionSortSolution:

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[1+1:r+1] = data[1:r]
                    data[l] = temp
        return data
