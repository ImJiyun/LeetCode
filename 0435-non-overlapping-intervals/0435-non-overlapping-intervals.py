class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        cnt = 0

        for start, cur_end in intervals[1:]:
            if start < end:
                cnt += 1
            else:
                end = cur_end
        return cnt            