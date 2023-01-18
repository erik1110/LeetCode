'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        l = 0
        while True:
            try:
                myList = [item[l] for item in strs]
            except IndexError:
                break
            if all(x==myList[0] for x in myList):
                prefix += myList[0]
            else:
                break
            l += 1

        return prefix