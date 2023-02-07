'''
102. Binary Tree Level Order Traversal
BFS

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            queue_len = len(queue)
            temp = []
            for _ in range(queue_len):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res