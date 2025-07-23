class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # - 4 -1 -1 0 1 2
        nums.sort()
        ans = []

        for left in range(0, len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid, right = left + 1, len(nums)-1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total < 0:
                    mid += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1    
        return ans   
