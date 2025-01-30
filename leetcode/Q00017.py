class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        combinations = []

        def backtracking(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            letters = letters_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtracking(index+1, path)
                path.pop()
        backtracking(0, [])
        return combinations
