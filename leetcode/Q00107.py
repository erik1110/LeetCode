'''
107. Binary Tree Level Order Traversal II

BFS

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q = deque()
        q.append(root)

        res = deque()
        while q:
            q_len = len(q)
            temp = []
            for _ in range(q_len):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.appendleft(temp)
        return res
