'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1=Counter(s1)
        n=len(s1)
        for i in range(len(s2)-len(s1)+1):
            h2 = Counter(s2[i:i+n])
            if h1==h2:
                return True
        return False