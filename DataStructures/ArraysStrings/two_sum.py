'''
Given an array, find the two indices that sum to a specific value

Constraints
    There is exactly one solution
    The array is an array of ints
    The array is not sorted
    Negative values are possible
    We cannot assume the inputs are valid
    We assume this fits in memory

Test Cases
    None input -> TypeError
    [] -> ValueError
    [1, 3, 2, -7, 5], 7 -> [2, 4]
'''
# Implement
class SumIndex:

    def two_sum(self, nums, target):

        # TODO: Implement me
        pass


# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestTwoSum(object):

    def test_two_sum(self):
        solution = Solution()
        assert_raises(TypeError, solution.two_sum, None, None)
        assert_raises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()

'''
Complexity:
    Time: O(n)
    Space: O(n)
'''

# Solution
class SumIndexSolution:

    def two_sum(self, nums, target):
        if nums is None or target is None:
            raise TypeError('nums or target cannot be None')
        if nums == []:
            raise ValueError('nums cannot be empty')

        answer = []
        for idx, num in enumerate(nums):
            if target - num in nums:
                answer.append(idx)
        return answer
