from collections import defaultdict

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = defaultdict(int)
        left, right, total, max_sum, N = 0, 0, 0, 0, len(nums)

        while right < N:
            cnts[nums[right]] += 1
            total += nums[right]
            while cnts[nums[right]] > 1:
                cnts[nums[left]] -= 1
                total -= nums[left]
                left += 1
            max_sum = max(max_sum, total)
            right += 1  

        return max_sum    