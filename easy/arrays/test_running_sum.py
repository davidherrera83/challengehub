import pytest
from running_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    nums = [1, 2, 3, 4]
    expected = [1, 3, 6, 10]
    assert solution.runningSum(nums) == expected


def test_example2(solution):
    nums = [1, 1, 1, 1, 1]
    expected = [1, 2, 3, 4, 5]
    assert solution.runningSum(nums) == expected


def test_example3(solution):
    nums = [3, 1, 2, 10, 1]
    expected = [3, 4, 6, 16, 17]
    assert solution.runningSum(nums) == expected
