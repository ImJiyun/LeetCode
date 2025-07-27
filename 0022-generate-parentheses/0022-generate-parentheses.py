class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        cnt = {'(': 0, ')': 0}

        def dfs(string, open_cnt, close_cnt):
            if len(string) == 2 * n:
                ans.append(string)
                return
            
            if open_cnt < n:
                dfs(string+'(', open_cnt+1, close_cnt)
            if open_cnt > close_cnt:
                dfs(string+')', open_cnt, close_cnt+1)    

        dfs('', 0, 0)
        return ans        