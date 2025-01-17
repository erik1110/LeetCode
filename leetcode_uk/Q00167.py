class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            number_sum = numbers[left] + numbers[right]
            if number_sum == target:
                return [left+1, right+1]
            elif number_sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
