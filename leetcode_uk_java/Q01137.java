class Solution {
    public int tribonacci(int n) {
        List<Integer> list = new ArrayList<>();
        list.add(0);
        list.add(1);
        list.add(1);

        if (n == 0) {
            return list.get(0);
        } else if (n == 1) {
            return list.get(1);
        } else if (n == 2) {
            return list.get(2);
        } else {
            int temp;
            for (int i = 3; i <= n; i++) {
                temp = list.get(i-3) + list.get(i-2) + list.get(i-1);
                list.add(temp);
            }
            return list.get(n);
        }
    }
}