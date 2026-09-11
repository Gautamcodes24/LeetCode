class Solution:
    def __init__(self):
        self.direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
        def dfs(r , c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or visit[r][c]:
                return
            visit[r][c] = True
            for dr,dc in self.direction:
                dfs(r+dr,c+dc)
        for i in range(rows):
            for j in range(cols):
                # is it a border
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == 1:
                    dfs(i, j)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visit[i][j]:
                   count += 1
        return count

        
