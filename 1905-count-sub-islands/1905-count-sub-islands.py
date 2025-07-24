from collections import deque

class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        cnt = 0
        N, M = len(grid2), len(grid2[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = [[False] * M for _ in range(N)]

        def bfs(q, arr):
            while q:
                r, c = q.popleft()
                
                for dr, dc in dir:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nr > N-1 or nc < 0 or nc > M-1 or visited[nr][nc] or not grid2[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc)) 
                    arr.append((nr, nc))    

        def check(arr):
            for r, c in arr:
                if grid1[r][c] == 0:
                    return False
            return True

        for r in range(N):
            for c in range(M):
                if grid2[r][c] == 1 and not visited[r][c]:
                    q = deque([(r, c)])
                    arr = [(r, c)]
                    visited[r][c] = True
                    bfs(q, arr)
                    if check(arr):
                        cnt += 1
        return cnt