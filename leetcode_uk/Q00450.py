'''
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Notes:
1. This problem can be solved by recursive method.
2. If you found the node has no `left` and no `right` children (a left node), then it will return None
3. If you found the node has `left` and no `right` children, then it will return `left`.
4. If you found the node has no `left` and `right` children, then it will return `right`

For example, step 3 helps you to get rid of the node (3) you found, then it will return `left` child.
key = 3
    5
   / \
  3   6
 /     \
2       7 

You can just return left child.
    5
   / \
  2   6
       \
        7 
 
5. If you found the node has `left` and `right` children, then you can assume to find the min of the right subtree.
For example, you won't know node 4 whether is has leaf or not, so you need to use recursive method.
key = 3
    10
   / \
  3   8
 / \   \
2   6   9 
   / \
  5   7


Find the min of this subtree, this is 5. (recursively find the left node because it is binary tree.)
Since 5 is a leaf node (it has no children), the algorithm simply removes it by returning None for this node.
    10
   /  \
  5    8
 / \    \
2   6    9
      \
       7

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # find the node to remove
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                # find the min from right subree
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
        return root                
