from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visited = [False] * N
        q = deque([0])

        while q:
            node = q.popleft()
            visited[node] = True

            for neighbor in rooms[node]:
                if not visited[neighbor]:
                    q.append(neighbor)  

        return len([i for i in visited if i]) == N