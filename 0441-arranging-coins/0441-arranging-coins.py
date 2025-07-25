class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        
        L, R = 0, n

        while L <= R:
            M = (L+R) // 2
            coins = M * (M+1) // 2

            if n == coins:
                return M
            elif n < coins:
                R = M-1
            else:
                L = M+1

        return R             