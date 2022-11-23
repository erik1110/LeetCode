'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, ele in enumerate(s):
            if i == 0:
                sub = s[1:]
            elif i == len(s):
                sub = s[:-1]
            else:
                sub = s[0:i] + s[i+1:len(s)]
            if ele not in sub:
                return i
        return -1