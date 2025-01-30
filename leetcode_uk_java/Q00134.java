class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_tank = 0;
        int curr_tank = 0;
        int start = 0;
        for (int i=0; i < gas.length; i++){
            int net = gas[i] - cost[i];
            total_tank += net;
            curr_tank += net;
            if (curr_tank < 0) {
                start = i + 1;
                curr_tank = 0;
            }
        }
        if (total_tank >= 0) {
            return start;
        } else {
            return -1;
        }
    }
}
