'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
'''
class Solution:            
    def search(self, nums: List[int], target: int) -> int:
        # left pointer
        start=0  
        # right pointer
        end=len(nums)-1
        # until both comes not equal
        while start<=end:
            mid=(start+end) // 2      # Calculating mid point
            # checking if mid is target then return  index
            if nums[mid]==target:
                return mid
            #   checking first half array is sorted or not
            elif nums[mid]>=nums[start]:
                # checking target is exist in first half or not
                if (target>=nums[start] and target<nums[mid]):
                    end=mid-1
                else:
                    start=mid+1
            else:
                # checking for target exist in second half or not
                if (target<=nums[end] and target>nums[mid]):
                    start=mid+1
                else:
                    end=mid-1
        return -1