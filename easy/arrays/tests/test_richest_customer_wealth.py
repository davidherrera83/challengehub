import pytest
from easy.arrays.richest_customer_wealth import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example1(solution):
    accounts = [[1, 2, 3], [3, 2, 1]]
    expected = 6
    assert solution.maximumWealth(accounts) == expected

def test_example2(solution):
    accounts = [[1, 5], [7, 3], [3, 5]]
    expected = 10
    assert solution.maximumWealth(accounts) == expected

def test_example3(solution):
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    expected = 17
    assert solution.maximumWealth(accounts) == expected