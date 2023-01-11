'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        my_s = []
        for i in s:
            if i != '#':
                my_s.append(i)
            else:
                my_s.pop() if my_s else None

        my_t = []
        for j in t:
            if j != '#':
                my_t.append(j)
            else:
                my_t.pop() if my_t else None 
        
        ss = ''.join(my_s)
        tt = ''.join(my_t)

        if ss == tt:
            return True
        return False
