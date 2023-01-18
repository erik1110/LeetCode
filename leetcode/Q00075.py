'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        twos = 0
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            if i == 1:
                ones += 1
            if i == 2:
                twos += 1
        for i in range(len(nums)):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
            elif ones != 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
                twos -= 1