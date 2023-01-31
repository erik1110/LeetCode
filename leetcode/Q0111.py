'''
111. Minimum Depth of Binary Tree
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + rightDepth
        elif root.right is None:
            return 1 + leftDepth
        return min(leftDepth, rightDepth) + 1
