import pytest
from easy.arrays.steps_to_zero import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example1(solution):
    num = 14
    expected = 6
    assert solution.numberOfSteps(num) == expected

def test_example2(solution):
    num = 8
    expected = 4
    assert solution.numberOfSteps(num) == expected

def test_example3(solution):
    num = 123
    expected = 12
    assert solution.numberOfSteps(num) == expected
