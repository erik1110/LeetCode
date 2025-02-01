class Solution {
    private List<List<Integer>> combinations = new ArrayList<>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        backtracking(1, new ArrayList<>(), k, n, 0);

        return combinations;
    }

    public void backtracking(int index, List<Integer> now, int k, int n, int sum) {
            if (sum > n) return;
            if (now.size() > k) return;
            if (sum == n && now.size() == k) {
                combinations.add(new ArrayList<>(now));
                return;
            }

            for (int i=index; i <= 9; i++) {
                now.add(i);
                backtracking(i+1, now, k, n, sum+i);
                now.remove(now.size()-1);
            }
    }
}
