'''
912. Sort an Array
Medium

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left_array = nums[:mid]
        right_array = nums[mid:]

        left_array = self.sortArray(left_array)
        right_array = self.sortArray(right_array)

        return self.mergeArray(left_array, right_array)
    
    def mergeArray(self, left_array, right_array):
        result = []
        i = 0
        j = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                result.append(left_array[i])
                i += 1
            else:
                result.append(right_array[j])
                j += 1
        result += left_array[i:]
        result += right_array[j:]

        return result

