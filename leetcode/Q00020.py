'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_tup = tuple("([{")
        close_tup = tuple(")]}")
        map = dict(zip(open_tup, close_tup))
        for i in s:
            if i in open_tup:
                stack.append(map[i])
            elif i in close_tup:
                if not stack or i!=stack.pop():
                    return False

        if stack:
            return False
        return True

## my solution

class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in s:
            # left
            if i == "(":
                queue.append(")")
            elif i == "[":
                queue.append("]")
            elif i == "{":
                queue.append("}")
            # right
            if i == ")":
                if queue and queue[-1] == ")":
                    queue.pop()
                else:
                    return False
            elif i == "]":
                if queue and queue[-1] == "]":
                    queue.pop()
                else:
                    return False
            elif i == "}":
                if queue and queue[-1] == "}":
                    queue.pop()
                else:
                    return False
        if queue:
            return False
        else:
            return True
