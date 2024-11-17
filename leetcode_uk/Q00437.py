'''
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

For example, targetSum = 3
    1
  /  \
 2    3

- Step 1:

        1
       / 
    For left tree
    count_path(curr_node=1, targetSum=3, curr_path=[])
    curr_path = [1]
    left tree -> count_path(curr_node=2, targetSum=3, curr_path=[1])

- Step 2:

       1
      /  
    2   
    count_path(curr_node=2, targetSum=3, curr_path=[1])
    curr_path = [1, 2]
    path_count += 1 -> return path_count
    left tree -> count_path(curr_node=None, targetSum=3, curr_path=[1, 2]) return 0
    right tree -> count_path(curr_node=None, targetSum=3, curr_path=[1, 2]) return 0

- Step 3:

        1
       / 
    back to node 1
    path_count += count_path(curr_node=2, targetSum=3, curr_path=[1])
    now path_count is 1

- Step 4:

        1
         \
    For right tree
    path_count += count_path(curr_node=3, targetSum=3, curr_path=[1])
    it will return path_count is 0 (Follow Step 2 ~ 3 again)
    so finally we get path_count is 1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def count_path(curr_node, targetSum, curr_path):
            if not curr_node:
                return 0
            curr_path.append(curr_node.val)
            path_count = 0
            path_sum = 0

            for i in range(len(curr_path) -1, -1, -1):
                path_sum += curr_path[i]
                if path_sum == targetSum:
                    path_count += 1
            
            path_count += count_path(curr_node.left, targetSum, curr_path)
            path_count += count_path(curr_node.right, targetSum, curr_path)
            curr_path.pop()
            return path_count
        return count_path(root, targetSum, [])
