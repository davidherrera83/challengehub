"""
Running Sum of 1-Dimensional Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []  # Initialize an empty list called runningSum.

        current_sum = 0  # Keep track of the running sum.

        for num in nums:  # Iterate through each element in the input array nums
            current_sum += num  # Add the current element to current_sum.
            runningSum.append(current_sum)  # Append current_sum to the runningSum list.

        return runningSum  # Return the runningSum list as the final output.
