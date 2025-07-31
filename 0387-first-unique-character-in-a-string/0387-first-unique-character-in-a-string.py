from collections import deque

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = deque()
        visited = set()

        for ch in s:
            if ch not in visited:
                visited.add(ch)
                queue.append(ch)
            else:
                if ch in queue:
                    queue.remove(ch)
        return s.index(queue[0]) if queue else -1            