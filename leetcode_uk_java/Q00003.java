class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int left = 0, right = 0, maxLen = 0;

        while (right < s.length()) {
            char c = s.charAt(right);
            if (!set.contains(c)) {
                set.add(c);
                right++;
                maxLen = Math.max(maxLen, right - left);
            } else {
                set.remove(s.charAt(left));
                left++;
            }
        }

        return maxLen;
    }
}