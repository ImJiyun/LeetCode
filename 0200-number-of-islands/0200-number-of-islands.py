from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(grid), len(grid[0])
        visited = [[False] * M for _ in range(N)]
        cnt = 0

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            visited[start_r][start_c] = True

            while q:
                r, c = q.popleft()

                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or grid[nr][nc] == '0' or visited[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    cnt += 1
        return cnt            