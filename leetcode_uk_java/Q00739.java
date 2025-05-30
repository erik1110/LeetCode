class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<>();
        int[] res = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > stack.peek()[1]) {
                int[] top = stack.pop();
                res[top[0]] = i - top[0];
            }
            stack.push(new int[]{i, t});
        }
        return res;
    }
}