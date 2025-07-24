from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(maze), len(maze[0])
        start_r, start_c = entrance[0], entrance[1] 
        q = deque([(start_r, start_c, 0)])
        visited = [[False] * M for _ in range(N)]
        visited[start_r][start_c] = True

        while q:
            r, c, dist = q.popleft()

            if (r != start_r or c != start_c) and (r == 0 or r == N-1 or c == 0 or c == M-1):
                return dist

            for dr, dc in dir:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr > N-1 or nc < 0 or nc > M-1 or maze[nr][nc] == '+' or visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc, dist+1))    

        return -1