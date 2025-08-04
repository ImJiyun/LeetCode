class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        dp = [0] * N
        if N >= 2:
            dp[0], dp[1] = nums[0], nums[1]
        elif N >= 1:
            dp[0] = nums[0]
        else:
            return []        

        for i in range(N):
            for j in range(i+2, N):
                print(i, j)
                dp[j] = max(dp[j], dp[i]+nums[j])

        return max(dp[N-1], dp[N-2])        