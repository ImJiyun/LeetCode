class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # live : < 2 live -> die
        # live : 2 or 3 live -> live
        # live: > 3 live -> die
        # dead: 3 live -> live

        ones = []
        N, M = len(board), len(board[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def check_border(r, c):
            num = 0
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
                    continue
                if board[nr][nc] == 1:
                    num += 1    

            if board[r][c] == 1:
                if 2 <= num <= 3:
                    ones.append((r, c))
            else:
                if num == 3:
                    ones.append((r, c))

        for r in range(N):
            for c in range(M):
                check_border(r, c)

        for r in range(N):
            for c in range(M):
                if (r, c) in ones:
                    board[r][c] = 1
                else:
                    board[r][c] = 0            
