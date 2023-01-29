'''
1189. Maximum Number of Balloons
Easy

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
 

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2

'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count("b")
        a = text.count("a")
        l = text.count("l") // 2
        o = text.count("o") // 2
        n = text.count("n")

        return min(b, a, l, o, n)
