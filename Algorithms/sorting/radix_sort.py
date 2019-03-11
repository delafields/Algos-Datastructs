'''
Implement radix sort

Constraints
    The input is a list
    Check for None in place of an array
    Assume array elements are ints
    We do not know the max digits to handle
    The digits are base 10
    Assume it fits in memory

Test Cases
    None -> Exception
    [] -> []
    [128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]
'''
# Implement

class RadixSort:

    def sort(self, array, base=10):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestRadixSort(object):

    def test_sort(self):
        radix_sort = RadixSort()
        assert_raises(TypeError, radix_sort.sort, None)
        assert_equal(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        assert_equal(radix_sort.sort(array), expected)
        print('Success: test_sort')


def main():
    test = TestRadixSort()
    test.test_sort()


if __name__ == '__main__':
    main()

'''
Algorithm
    Sample input: [1, 220, 122, 112]

    We'll evaluate each digit starting with the ones position
        [!1, 22!0, 12!2, 11!2]
            Bucket 0: 220
            Bucket 1: 1
            Bucket 2: 122, 112
            Result: [220, 1, 122, 112]
        [22!0, 1, 12!2, 11!2]
            Bucket 0: 1
            Bucket 1: 112
            Bucket 2: 220, 122
            Result: [1, 112, 220, 122]
        [1, 1!12, 2!20, 1!22]
            Bucket 0: 1
            Bucket 1: 112, 122
            Bucket 2: 220
            Result: [1, 112, 122, 220]

    Bucketing example: 123
        Ones
            123 // 10^0 = 123
            123 % 10 = 3
        Tens
            123 // 10^1 = 12
            12 % 10 = 2
        Hundreds
            123 // 10^2 = 1
            1 % 10 = 1

    Complexity:
        Time: O(k * n) where n is the number of items
              and k is the number of digits in the largest item
        Space: O(k + n)

    Notes:
        Not in place
        Most implementations are stable

        If k (the number of digits) is less than log(n), radix sort
        can be faster than algorithms such as quicksort
'''
# Solution

class RadixSortSolution:

    def sort(self, array, base=10):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return []

        max_element = max(array)
        max_digits = len(str(abs(max_element)))
        curr_array = array

        for digit in range(max_digits):
            buckets = [[] for _ in range(base)]:
            for item in curr_array:
                buckets[(item//(base**digit))%base].append(item)
            curr_array = []
            for bucket in buckets:
                curr_array.extend(bucket)
        return curr
