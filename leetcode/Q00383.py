'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        for s in list(ransomNote):
            try:
                m.remove(s)
            except:
                return False
        return True