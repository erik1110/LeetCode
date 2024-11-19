'''
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

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
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(left_arr, right_arr):
            result = []
            l = 0
            r = 0
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] < right_arr[r]:
                    result.append(left_arr[l])
                    l += 1
                else:
                    result.append(right_arr[r])
                    r += 1
            if l == len(left_arr):
                result.extend(right_arr[r:])
            else:
                result.extend(left_arr[l:])
            return result

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            else:
                m = len(arr) // 2
                left_array = arr[:m]
                right_array = arr[m:]
                return merge(mergeSort(left_array), mergeSort(right_array))

        return mergeSort(nums)
