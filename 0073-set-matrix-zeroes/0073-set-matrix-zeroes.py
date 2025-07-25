class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N, M = len(matrix), len(matrix[0])
        zeros = []

        # (0, 0), (0, 3)
        # set => 0
        # set => 0, 3

        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 0:
                    zeros.append((r, c))

        rows, cols = set(), set()

        for r, c in zeros:
            rows.add(r)
            cols.add(c)

        for r in rows:
            for c in range(M):
                matrix[r][c] = 0

        for c in cols:
            for r in range(N):
                matrix[r][c] = 0

        return matrix                    