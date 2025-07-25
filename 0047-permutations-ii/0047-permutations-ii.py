class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N = len(nums)
        ans, arr = [], []
        visited = [False] * N

        def dfs():
            if len(arr) == N:
                ans.append(arr[:])
            for i in range(N):
                if visited[i]:
                    continue

                # prevent duplicates
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                visited[i] = True    
                arr.append(nums[i])
                dfs()
                arr.pop()
                visited[i] = False

        dfs()
        return ans        