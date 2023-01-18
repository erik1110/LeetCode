'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        node = result
        while list1 or list2:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    node.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    node.next = ListNode(list2.val)
                    list2 = list2.next 
            elif list1 is None:
                node.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                node.next = ListNode(list1.val)
                list1 = list1.next
            node = node.next
        return result.next