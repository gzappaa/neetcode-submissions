class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        fresh = 0
        q = deque()


        def helper(r,c):
            nonlocal fresh
            if (r < 0 or r >= rows or c < 0 or c >= cols 
            or (r,c) in seen or grid[r][c] != 1):
                return 
            seen.add((r,c))
            q.append([r,c])
            fresh -= 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1


        time = 0        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                helper(r - 1, c)
                helper(r + 1, c)
                helper(r, c + 1)
                helper(r, c - 1)    
            time += 1

        return time if fresh == 0 else -1

                    
        