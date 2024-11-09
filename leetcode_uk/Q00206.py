# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1. origin: 1 -> 2 -> 3 -> 4 -> 5

2. add None, prev Node, curr Node
None   1  -> 2 -> 3 -> 4 -> 5
prev curr

None <- 1  X 2 -> 3 -> 4 -> 5
prev curr

None <- 1  X 2 -> 3 -> 4 -> 5
     prev curr

None <- 1  <- 2 X 3 -> 4 -> 5
     prev curr

...

until curr is None
    
'''

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        return prev
