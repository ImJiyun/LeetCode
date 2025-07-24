from collections import deque, defaultdict

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)
        in_degree = [0] * N
        reversed_graph = defaultdict(list)

        for u in range(N):
            for w in graph[u]:
                reversed_graph[w].append(u)
            in_degree[u] = len(graph[u])

        q = deque([i for i in range(N) if in_degree[i] == 0])

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)

            for prev_node in reversed_graph[node]:
                in_degree[prev_node] -= 1
                if in_degree[prev_node] == 0:
                    q.append(prev_node)

        ans.sort()
        return ans
            