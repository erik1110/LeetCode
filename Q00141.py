'''
141. Linked List Cycle

141. Linked List Cycle
Easy

10698

913

Add to List

Share
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
# dictionary
#         temp = {}
        
#         while head:
#             if head in temp:
#                 return True
#             if head is not None:
#                 temp[head] = 1
#                 head = head.next
#         return False
# set
#         current = head
#         lookup = set()
        
#         while current:
#             if current in lookup: return True
#             lookup.add(current)
#             current = current.next
#         return False
    
    # Fast and Slow pointers 36%    
        if not head:
            return False
        
        def find_meet(head: ListNode) -> ListNode:
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return "cycle"
            return "not-cycle"
        
        meet_point = find_meet(head)
        new_point = head
        
        if meet_point == 'cycle':
            return True
        return False
