from collections import deque

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(land), len(land[0])
        visited = [[False] * M for _ in range(N)]
        q = deque()
        ans = []

        def bfs(start_r, start_c):
            while q:
                r, c, k = q.popleft()

                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr > N-1 or nc < 0 or nc > M-1 or visited[nr][nc] or land[nr][nc] == 0:
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc, k+1))    

                if len(q) == 0:
                    ans.append([start_r, start_c, r, c])

        for r in range(N):
            for c in range(M):
                if land[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c, 0))
                    bfs(r, c)

        return ans            