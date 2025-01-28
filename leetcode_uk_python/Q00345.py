'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        s = list(s)
        r = len(s) - 1
        vowel = ["a", "e", "i", "o", "u"]
        while l <= r:
            if s[l].lower() in vowel and s[r].lower() in vowel:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
            elif s[l].lower() in vowel and not s[r].lower() in vowel:
                r -= 1
            elif not s[l].lower() in vowel and s[r].lower() in vowel:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)
