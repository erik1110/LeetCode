class Solution {
    public int maxOperations(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int value;
        int count = 0;

        for (int num: nums) {
            value = k - num;
            if (map.containsKey(value) && map.get(value) > 0) {
                count++;
                map.put(value, map.get(value) - 1);
            } else {
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
        }
        return count;
    }
}