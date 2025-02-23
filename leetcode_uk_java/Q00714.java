class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int [] hold = new int[n];
        int [] cash = new int[n];

        hold[0] = -prices[0];
        cash[0] = 0;

        for (int i = 1; i < n; i++) {
            hold[i] = Math.max(hold[i-1], cash[i-1] - prices[i]);
            cash[i] = Math.max(cash[i-1], hold[i-1] + prices[i] - fee);
        }
        return cash[n-1];
        
    }
}
