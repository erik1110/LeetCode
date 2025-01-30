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
    public int maxLevelSum(TreeNode root) {
        int maxValue = Integer.MIN_VALUE;
        int maxLevel = 0;
        List<TreeNode> currLevel = new ArrayList();

        if (root != null) {
            currLevel.add(root);
        }
        int level = 0;
        while (!currLevel.isEmpty()){
            level += 1;
            int totalLevel = 0;
            List<TreeNode> nextLevel = new ArrayList();
            for (TreeNode node: currLevel) {
                totalLevel += node.val;
                if (node.left != null) {
                    nextLevel.add(node.left);
                }
                if (node.right != null) {
                    nextLevel.add(node.right);
                }
            }

            if (totalLevel > maxValue) {
                maxLevel = level;
                maxValue = totalLevel;
            }
            System.out.println("maxLevel:" + maxLevel);
            System.out.println("maxValue:" + maxValue);
            currLevel = nextLevel;
        }
        return maxLevel;
    }
}
