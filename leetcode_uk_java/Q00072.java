class Solution {
    public int minDistance(String word1, String word2) {
        int[][] grid = new int[word1.length()+1][word2.length()+1];

        for (int i=0; i<word1.length(); i++){
            grid[i][word2.length()] = word1.length() - i;
        }

        for (int i=0; i<word2.length(); i++){
            grid[word1.length()][i] = word2.length() - i;
        }

        for (int i=word1.length()-1; i >= 0; i--){
            for (int j=word2.length()-1; j >= 0; j--){
                if (word1.charAt(i) == word2.charAt(j)) {
                    grid[i][j] = grid[i+1][j+1];
                } else {
                    grid[i][j] = Math.min(Math.min(grid[i + 1][j], grid[i + 1][j + 1]), grid[i][j + 1]) + 1;
                }
            }
        }

        return grid[0][0];
    }
}
