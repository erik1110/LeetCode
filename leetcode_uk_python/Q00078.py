class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.nums = nums
        self.n = len(nums)
        self.backtrack(0, [])
        return self.output

    def backtrack(self, start, curr):
        self.output.append(list(curr))
        for i in range(start, self.n):
            curr.append(self.nums[i])
            self.backtrack(i+1, curr)
            curr.pop()
