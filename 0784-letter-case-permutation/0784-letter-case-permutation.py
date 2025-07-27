class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        N = len(s)

        def dfs(idx, string):
            if idx == N:
                ans.append(string)
                return

            if s[idx].isdigit():
                dfs(idx+1, string+s[idx])
            else:
                dfs(idx+1, string+s[idx].lower())
                dfs(idx+1, string+s[idx].upper())
        dfs(0, "")
        return ans