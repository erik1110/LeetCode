class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(" ")
        result = []
        while split:
            if split[-1] != "":
                result.append(split.pop())
            else:
                split.pop()
        return " ".join(result)
