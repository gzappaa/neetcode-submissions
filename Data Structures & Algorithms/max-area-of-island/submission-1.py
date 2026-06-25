class Solution:
    def __init__(self):
        self.temp = 0
        self.maxisland = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
            or grid[r][c] == 0):
                return

            self.temp += 1
            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    self.maxisland = max(self.maxisland, self.temp)
                    self.temp = 0
                        
        return self.maxisland

        