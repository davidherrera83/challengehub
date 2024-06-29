import pytest
from easy.arrays.fizzbuzz import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example1(solution):
    n = 3
    expected = ["1", "2", "Fizz"]
    assert solution.fizzBuzz(n) == expected

def test_example2(solution):
    n = 5
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    assert solution.fizzBuzz(n) == expected

def test_example3(solution):
    n = 15
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert solution.fizzBuzz(n) == expected
