"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional

class ListNode:
    # Defines the structure of a node in the linked list. https://www.geeksforgeeks.org/python-linked-list/#
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head # slow moves one step at a time.
        fast = head # fast moves two steps at a time.
        
        while fast and fast.next: # When fast reaches the end, slow is at the middle.
            slow = slow.next
            fast = fast.next.next
        
        return slow