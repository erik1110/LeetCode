'''
Find the n adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

given an non-negative array
'''
class Solution:
    def maxProduct(self, nums: list, n: int) -> int:
        start = 0
        end = n
        max_product = 1
        while end <= len(nums):
            currentProduct = 1
            for i in range(start, end):
                currentProduct = currentProduct * nums[i]
            if currentProduct > max_product:
                max_product = currentProduct
            start += 1
            end += 1
        return max_product
    

s = Solution()
s.maxProduct([1, 3, 5, 7, 6, 0, 1055, 0], 3)
