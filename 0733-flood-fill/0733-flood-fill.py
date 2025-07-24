from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(image), len(image[0])
        q = deque([(sr, sc)])
        visited = [[False] * M for _ in range(N)]
        visited[sr][sc] = True

        while q:
            r, c = q.popleft()
            
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr > N-1 or nc < 0 or nc > M-1 or visited[nr][nc] or image[nr][nc] != image[sr][sc]:
                    continue
                visited[nr][nc] = True
                image[nr][nc] = color
                q.append((nr, nc)) 
    
        image[sr][sc] = color

        return image
        