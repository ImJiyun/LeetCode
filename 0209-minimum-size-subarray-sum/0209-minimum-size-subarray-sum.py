class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, total, N = 0, 0, 0, len(nums)
        min_len = float('inf')

        while right < N:
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0