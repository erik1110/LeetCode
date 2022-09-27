'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 

No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if self.check(s) == self.check(t):
            return True
        return False
    def check(self, text): 
        temp = []
        count = 1
        repo = {}
        for i, ele in enumerate(text):
            if ele in repo.keys():
                temp.append(repo[ele])
            else:
                temp.append(count)
                repo[ele] = count
                count += 1
        return temp