class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length()!=word2.length()){
            return false;
        }

        int[] count1 = new int[26];
        int[] count2 = new int[26];
        Set<Character> set1 = new HashSet<>();
        Set<Character> set2 = new HashSet<>();

        for (char c : word1.toCharArray()){
            count1[c - 'a']++;
            set1.add(c);
        }
        for (char c : word2.toCharArray()){
            count2[c - 'a']++;
            set2.add(c);
        }
        if (!set1.equals(set2)){
            return false;
        }

        Arrays.sort(count1);
        Arrays.sort(count2);
        return Arrays.equals(count1, count2);
    }
}