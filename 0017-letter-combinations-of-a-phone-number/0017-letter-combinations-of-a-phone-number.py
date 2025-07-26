class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digits_alpha = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        output = []
        N = len(digits)
        
        def dfs(idx, string):
            if idx == N:
                output.append(string)
                return 
            alpha_arr = digits_alpha[digits[idx]]
            for i in range(len(alpha_arr)):
                dfs(idx + 1, string + alpha_arr[i])
        dfs(0, "")

        return output