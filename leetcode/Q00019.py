'''
19. Remove Nth Node From End of List

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode()
        node = result
        
        temp = []
        
        while head:
            if head is not None:
                temp.append(head.val)
                head = head.next
        temp.pop(-n)
        
        for t in temp:
            node.next = ListNode(t)
            node = node.next
        return result.next