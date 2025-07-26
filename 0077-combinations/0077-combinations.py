class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans, arr = [], []

        def dfs(start):
            if len(arr) == k:
                ans.append(arr[:])
                return 

            for i in range(start, n+1):
                arr.append(i)
                dfs(i+1)
                arr.pop()

        dfs(1)        
        return ans        