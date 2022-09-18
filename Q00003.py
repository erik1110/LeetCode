'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub_str = ''
        max_len = 0
        
        for w in s:
            print("="*5)
            print("sub_str:", sub_str)
            while w in sub_str:
                print("w:", w)
                sub_str = sub_str[1:]
                print("sub_str:", sub_str)
            else:
                sub_str += w
                max_len = max(len(sub_str), max_len)
        
        return max_len