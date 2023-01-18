'''
566. Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        # check legal
        if m*n != r*c:
            return mat
        d1 = []
        
        # 2d to 1d
        for i in range(m):
            for j in range(n):
                d1.append(mat[i][j])

        
        new_mat = []
        temp = []
        
        # 1d to 2d
        for i in range(len(d1)):
            temp.append(d1[i])
            if (i+1) % c == 0:
                new_mat.append(temp)
                temp = []

        return new_mat