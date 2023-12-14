'''
Write a function called minSubLength which accepts two parameters, an array of
positive integers and a positive integers. This function should return the minimal
length of a continuous subarray - the sum of elements inside this subarray has to
be greater than or equal the positive integer parameter. If subarray not found,
then return 0.
'''
def minSubLength(nums, target):
    left = 0
    right = 0
    # I add 1 because it is impossible to happen
    minLength = len(nums) + 1
    currentSum = 0
    while right <= len(nums):
        currentSum = sum(nums[left:right])
        while currentSum >= target:
            currentSum = sum(nums[left:right])
            if minLength > (right-left+1):
                minLength = right-left+1
            left += 1
        right += 1
    if minLength == len(nums) + 1:
        return 0
    return minLength

nums = [8, 1, 6, 15, 3, 16, 5, 7, 14, 30, 12]
target = 60

minSubLength(nums, target)
# 4