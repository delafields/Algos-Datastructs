'''
Implement selection sort

Constraints
    A naive solution is sufficient (ie not stable, not based on a heap)
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

class SelectionSort:

    def sort(self, data):
        # TODO: Implement me (recursive)
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestSelectionSort(object):

    def test_selection_sort(self, func):
        print('None input')
        assert_raises(TypeError, func, None)

        print('Empty input')
        assert_equal(func([]), [])

        print('One element')
        assert_equal(func([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        assert_equal(func(data), sorted(data))

        print('Success: test_selection_sort\n')


def main():
    test = TestSelectionSort()
    selection_sort = SelectionSort()
    test.test_selection_sort(selection_sort.sort)
    try:
        test.test_selection_sort(selection_sort.sort_recursive)
        test.test_selection_sort(selection_sort.sor_iterative_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()

'''
Algorithm
    We can do this recursively or iteratively
        Iteratively will be more efficient as it doesn't require
        the extra space overhead with the recursive calls

    For each element
        Check every element to the right and find the min
        If min < current element
            Swap

    Complexity:
        Time: O(n^2) average/worst/best
        Space: O(1) iterative, O(m) recursive where m is the recursion depth (unless tail-call elimination is available, then O(1))

    Notes:
        In-place
        Most implementations are not stable, due to swapping of values

        Selection sort might be a good option if moving elements is more expensive
        than comparing them, as it requires at most n-1 swaps

        Finding of a min element can be done with a min-heap, which would
        change the worst-case run time to O(n log n) and increase the space
        to O(n). This is called a heap sort
'''
# Solution

class SelectionSortSolution:

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
                if data[min_index] < data[i]:
                    data[i], data[min_index] = data[min_index], data[i]
        return data

    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def sort_recursive(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive
        if data is None:
            raise TypeError('data cannot be None')
        if start < len(data) - 1:
            swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start+1)
        return data

    def _find_min_index(self, data, start):
        min_index = start
        for i in range(start+1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data
