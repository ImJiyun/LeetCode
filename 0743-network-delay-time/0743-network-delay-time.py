from collections import defaultdict
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        distances = [float('inf')] * (n+1)
        distances[0], distances[k] = 0, 0

        for u, v, w in times:
            graph[u].append((v, w))

        queue = []
        heapq.heappush(queue, (0, k))   

        while queue:
            dist, node = heapq.heappop(queue)

            if dist < distances[node]:
                continue

            print(distances)    
            for neighbor, cost in graph[node]:
                new_cost = cost + dist
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))

        return max(distances) if max(distances) != float('inf') else -1