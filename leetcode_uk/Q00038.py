class Solution:
    def countAndSay(self, n: int) -> str:
        current_string = "1"
        if n == 1:
            return current_string
        for _ in range(n-1):
            current_string = self.rle(current_string)
        return current_string

    def rle(self, string):
        result = []
        i = 0
        while i != len(string):
            digit = string[i]
            count = 1
            i += 1
            while i != len(string) and digit == string[i]:
                count += 1
                i += 1
            result.append(str(count))
            result.append(digit)
        return "".join(result)
