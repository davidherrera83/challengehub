"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [] # answer is an empty list that will store the results.

        for i in range(1, n + 1): # Use a for loop to iterate through the range from 1 to n (inclusive).
            if i % 3 == 0 and i % 5 == 0: 
                answer.append("FizzBuzz") # If the current number i is divisible by both 3 and 5, append "FizzBuzz" to the list.
            elif i % 3 == 0:
                answer.append("Fizz") # If i is divisible by 3 but not 5, append "Fizz".
            elif i % 5 == 0:
                answer.append("Buzz") # If i is divisible by 5 but not 3, append "Buzz".
            else:
                answer.append(str(i)) # If i is not divisible by either 3 or 5, append the string representation of i.
        return answer
            