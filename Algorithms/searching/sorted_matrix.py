'''
Search a sorted matrix for an item

Constraints
    Items in each row are sorted
    Items in each column are sorted
    Sorted in ascending order
    The matrix is a rectangle, not jagged
    The matrix is not necessarily squared
    The output should be a tuple (row, col)
    The item isn't definitely in the matrix
    Don't assume the inputs are valid
    Assume this fits in memory

Test Cases
    None -> Exception
    General case
        Item found -> (row, col)
        Item not found -> None
'''
# Implement

class SortedMatrix:

    def find_val(self, matrix, val):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestSortedMatrix(object):

    def test_find_val(self):
        matrix = [[20, 40, 63, 80],
                  [30, 50, 80, 90],
                  [40, 60, 110, 110],
                  [50, 65, 105, 150]]
        sorted_matrix = SortedMatrix()
        assert_raises(TypeError, sorted_matrix.find_val, None, None)
        assert_equal(sorted_matrix.find_val(matrix, 1000), None)
        assert_equal(sorted_matrix.find_val(matrix, 60), (2, 1))
        print('Success: test_find_val')


def main():
    test = TestSortedMatrix()
    test.test_find_val()


if __name__ == '__main__':
    main()

'''
Algorithms
    Find 60 (val = 60)

    20      40      63      80
    30      50      80      90
    40      60      100     110
    50      65      105     150

    If the start of a col < val -> look left
    If the end of a col < val   -> look right
    If the start of a row > val -> look up
    If the start of a row < val -> look down

    If we start at the upper right corner, we just need these cases
        If the start of a col > val -> look left
        If the end of a row < val   -> look down

    Complexity:
        Time: O(n + m), where n and m are the matrix dimensions
        Space: O(1)
'''
# Solution

class SortedMatrixSolution:

    def find_val(self, matrix, val):
        if matrix is None or val is None:
            raise TypeError('matrix or val cannot be None')

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == val:
                return (row, col)
            elif matrix[row][col] > val:
                col -= 1
            else:
                row += 1
        return None
