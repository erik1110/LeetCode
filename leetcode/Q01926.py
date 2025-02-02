class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r = len(maze)
        c = len(maze[0])
        queue = deque()
        queue.append([entrance[0], entrance[1], 0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        step = 0
        # does not count as an exit since it is the entrance cell.
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            for _ in range(len(queue)):
                i, j, step = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0<= nj < c and maze[ni][nj] == ".":
                        if ni == 0 or nj == 0 or ni == r - 1 or nj == c - 1:
                            return step + 1
                        maze[ni][nj] = "+"
                        queue.append([ni, nj, step+1])
        return -1
