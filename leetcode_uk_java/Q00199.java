/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> rightSide = new ArrayList();
        List<TreeNode> currLevel = new ArrayList();

        if (root != null) {
            currLevel.add(root);
        }

        while (!currLevel.isEmpty()) {
            rightSide.add(currLevel.get(currLevel.size()-1).val);
            List<TreeNode> nextLevel = new ArrayList();
            for (TreeNode var: currLevel) {
                if (var.left != null) {
                    nextLevel.add(var.left);
                }
                if (var.right != null) {
                    nextLevel.add(var.right);
                }
            }
            currLevel = nextLevel;
        }
        return rightSide;
        
    }
}
