import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        visited = set()
        heap = []

        heapq.heappush(heap, (nums1[0]+ nums2[0], 0, 0))
        visited.add((0, 0))
        
        while heap and len(ans) < k:
            total, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and not (i+1, j) in visited:
                visited.add((i+1, j))
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            if j+1 < len(nums2) and not (i, j+1) in visited:
                visited.add((i, j+1))
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))

        return ans        