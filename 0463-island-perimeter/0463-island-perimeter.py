from collections import deque

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N , M = len(grid), len(grid[0])
        q = deque([])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * M for _ in range(N)]
        perimeter = 0
        found = False

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited[r][c] = True
                    found = True
            if found:
                break        

        while q:
            r, c = q.popleft()

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                # not in the range or water
                if nr < 0 or nr > N-1 or nc < 0 or nc > M-1 or grid[nr][nc] == 0:
                    perimeter += 1
                # land
                elif not visited[nr][nc] and grid[nr][nc] == 1:    
                    visited[nr][nc] = True
                    q.append((nr, nc))
                
        return perimeter            