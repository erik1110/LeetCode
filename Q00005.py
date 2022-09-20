'''
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r-l+1) > resLen :
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
            # even case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
        return res