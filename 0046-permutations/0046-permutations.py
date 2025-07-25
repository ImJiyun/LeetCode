class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, arr = [], []
        N = len(nums)
        visited = [False] * N

        def dfs():
            if len(arr) == N:
                ans.append(arr[:])
                return

            for i in range(N):
                if visited[i]:
                    continue
                visited[i] = True
                arr.append(nums[i])
                dfs()
                arr.pop()
                visited[i] = False    

        dfs()

        return ans