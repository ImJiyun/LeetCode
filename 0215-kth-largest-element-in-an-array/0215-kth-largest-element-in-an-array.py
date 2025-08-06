import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for _ in range(k):
            result = -heapq.heappop(heap)

        return result