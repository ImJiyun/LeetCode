class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(node, arr):
            if node == len(graph)-1:
                ans.append(arr)
                return
            for neighbor in graph[node]:
                dfs(neighbor, arr + [neighbor])

        dfs(0, [0])        
        return ans