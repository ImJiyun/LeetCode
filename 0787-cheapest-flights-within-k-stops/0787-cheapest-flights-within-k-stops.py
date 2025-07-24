from collections import defaultdict
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        distances = [[float('inf') ] * (k+2) for _ in range(n)]
        distances[src][0] = 0
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        q = [(0, src, 0)]

        while q:
            cost, node, stops = heapq.heappop(q)

            if cost > distances[node][stops] or stops > k+1:
                continue

            for neighbor, dist in graph[node]:
                new_cost = cost + dist
                if stops+1 <= k+1 and new_cost < distances[neighbor][stops+1]:
                    distances[neighbor][stops+1] = new_cost
                    heapq.heappush(q, (new_cost, neighbor, stops+1))

        return min(distances[dst]) if min(distances[dst]) != float('inf') else -1