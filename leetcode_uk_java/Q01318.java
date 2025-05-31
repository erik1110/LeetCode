class Solution {
    public int minFlips(int a, int b, int c) {
        int flips = 0;

        for (int i = 0; i < 32; i++) {
            int bitA = ( a >> i ) & 1;
            int bitB = ( b >> i ) & 1;
            int bitC = ( c >> i ) & 1;


            if ((bitA | bitB) == bitC) {
                continue;
            } else {
                if (bitC == 1) {
                    flips++;
                } else {
                    if (bitA == 1) flips++;
                    if (bitB == 1) flips++;
                }
            }
        }
        return flips;
    }
}