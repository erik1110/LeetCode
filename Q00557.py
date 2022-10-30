'''
557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        temp = []
        n = s.split(" ")
        for i in n:
            l = 0
            r = len(i) - 1
            x = list(i)
            while l < r:
                x[l], x[r] = x[r], x[l]
                l += 1
                r -= 1
            i = "".join(x)
            temp.append(i)
        return " ".join(temp)