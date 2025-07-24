from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre_courses = defaultdict(list)
        in_degree = [0] * numCourses

        for second, first in prerequisites:
            pre_courses[first].append(second)
            in_degree[second] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in pre_courses[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return len(result) == numCourses         




        