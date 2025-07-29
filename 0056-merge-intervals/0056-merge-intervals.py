class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:    
            prev = merged[-1]
            if start <= prev[1]:
                prev[1] = end
            else:
                merged.append([start, end])

        return merged                