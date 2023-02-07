'''
103. Binary Tree Zigzag Level Order Traversal

BFS

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        q = deque()
        q.append(root)
        left2right = True
        res = []

        while q:
            q_len = len(q)
            temp = deque()
            for _ in range(q_len):
                node = q.popleft()
                if left2right:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
            left2right = not left2right
        return res