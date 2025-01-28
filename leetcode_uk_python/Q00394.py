class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c != "]":
                stack.append(str(c))
            else:
                string = ""
                while stack[-1] != "[":
                    string += str(stack[-1])
                    stack.pop()
                string = string[::-1]
                # remove [
                stack.pop()
                # integer
                times = []
                while stack and stack[-1].isdigit():
                    times.append(int(stack[-1]))
                    stack.pop()
                k = 0
                for i in range(len(times)):
                    k += (10 ** i ) * times[i]
                # encoded_string
                string = k * string
                stack.extend(list(string))
        return ''.join(map(str, stack))
