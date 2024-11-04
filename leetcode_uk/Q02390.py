class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i, char in enumerate(s):
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        result = "".join(stack)
        return result
