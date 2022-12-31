'''
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows =  len(matrix)
        nCols = len(matrix[0])
        
        row = nRows-1
        col = 0
        
        while 0 <= row < nRows and 0 <= col < nCols:
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                col += 1
            else:
                row -= 1
        
        return False