'''
82. Remove Duplicates from Sorted List II
Medium
7.1K
186
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]

'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        cur = dummy

        while cur:
            # if next two nodes are duplicates, move the cur.next forward
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                temp = cur.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            # if next two nodes are not duplicates, mode the cur to cur.next
            else:
                cur = cur.next

        return dummy.next
        

