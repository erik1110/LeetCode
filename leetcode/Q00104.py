'''
104. Maximum Depth of Binary Tree
Easy

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        stack = [{"node": root, "depth": 1}]
        while len(stack) > 0:
            nodeInfo = stack.pop()
            node, depth = nodeInfo["node"], nodeInfo["depth"]
            if node is None:
                continue
            maxdepth = max(maxdepth, depth)
            stack.append({"node": node.left, "depth": depth+1})
            stack.append({"node": node.right, "depth": depth+1})
        return maxdepth
