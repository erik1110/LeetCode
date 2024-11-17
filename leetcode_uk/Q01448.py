'''
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
 
Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_path(curr_node, curr_path):
            if not curr_node:
                return 0
            curr_path.append(curr_node.val)
            path_count = 0
            max_value = max(curr_path)
            if max_value == curr_node.val:
                path_count += 1
            path_count += count_path(curr_node.left, curr_path)
            path_count += count_path(curr_node.right, curr_path)
            curr_path.pop()
            return path_count
        return count_path(root, [])
