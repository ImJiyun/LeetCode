class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        visited = set()
        k = 0

        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            k += 1
            if k == 3:
                return num

        return nums[0]        