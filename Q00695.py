'''
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        has_visited = []
        max_area = 0
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if grid[m][n] == 1:
                    self.area = 0
                    self.count(grid, m, n, has_visited)
                    max_area = max(self.area, max_area)

        return max_area
    
    def count(self, grid, m, n, has_visited):
        if m<0 or n<0 or m>=len(grid) or n>=len(grid[0]):
            return 0
        if [m, n] in has_visited:
            return 0
        has_visited.append([m, n])
        if grid[m][n] == 0:
            return 0
        if grid[m][n] == 1:
            self.area += 1
        self.count(grid, m+1, n, has_visited)
        self.count(grid, m-1, n, has_visited)
        self.count(grid, m, n+1, has_visited)
        self.count(grid, m, n-1, has_visited)