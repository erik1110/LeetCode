class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])
        fresh_orange = 0
        queue = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh_orange += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])

        if fresh_orange == 0:
            return 0

        minute = 0

        while queue:
            change = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if  0 <= (i + 1) < r and 0 <= j < c and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    fresh_orange -= 1
                    queue.append([i+1, j])
                    change = True
                if 0 <= i < r and 0 <= (j + 1) < c and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    fresh_orange -= 1
                    queue.append([i, j+1])
                    change = True
                if 0 <= i - 1 < r and 0 <= j < c and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    fresh_orange -= 1
                    queue.append([i-1, j])
                    change = True
                if 0 <= i < r and 0 <= (j - 1) < c and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    fresh_orange -= 1
                    queue.append([i, j-1])
                    change = True
            if change:
                minute += 1

        return minute if fresh_orange == 0 else -1
