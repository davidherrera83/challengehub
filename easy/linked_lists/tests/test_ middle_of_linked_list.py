import pytest
from easy.linked_lists.middle_of_linked_list import ListNode, Solution

@pytest.fixture
def solution():
    return Solution()

def list_to_linkedlist(arr):
    """
    Helper function that convert between Python lists into a singly linked list.
    """
    head = ListNode(arr[0]) # Creates the head node of the linked list with the first element of the list arr.
    current = head # Sets the current pointer to the head of the linked list.
    for val in arr[1:]: # Iterates through the rest of the elements in arr (starting from the second element).
        current.next = ListNode(val) # Creates a new node with the current value val and links it to the current node.
        current = current.next #  Moves the current pointer to the newly created node.
    return head

def linkedlist_to_list(node):
    """
    Helper function that convert a singly linked list into a Python list.
    """
    result = [] # Creates an empty list to store the values of the linked list nodes.
    while node: # Continues until node is None.
        result.append(node.val) # Appends the value of the current node to the result list.
        node = node.next # Moves the node pointer to the next node in the linked list.
    return result

def test_example1(solution):
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    expected = [3, 4, 5]
    middle = solution.middleNode(head)
    assert linkedlist_to_list(middle) == expected

def test_example2(solution):
    head = list_to_linkedlist([1, 2, 3, 4, 5, 6])
    expected = [4, 5, 6]
    middle = solution.middleNode(head)
    assert linkedlist_to_list(middle) == expected
