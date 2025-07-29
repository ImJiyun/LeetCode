class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        arr = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                arr.append(interval)
            elif interval[0] > newInterval[1]:
                arr.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                print(newInterval)
        arr.append(newInterval)
        return arr        