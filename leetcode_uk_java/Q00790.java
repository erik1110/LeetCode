class Solution {
    public int numTilings(int n) {
        int MOD = 1_000_000_007;
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (n == 2) return 2;

        long[] f = new long[n+1];
        long[] p = new long[n+1];
        f[0] = 1;
        f[1] = 1;
        p[1] = 0;

        for (int i = 2; i <= n ; i++) {
            f[i] = (f[i-1] + f[i-2] + 2 * p[i-1]) % MOD;
            p[i] = (p[i-1] + f[i-2]) % MOD;
        }

        return (int) f[n];

    }
}