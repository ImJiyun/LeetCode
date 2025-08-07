from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnts = defaultdict(int)

        for ch in t:
            cnts[ch] += 1 

        left, right, N = 0, 0, len(s)    
        min_len = float('inf')
        window_cnts = defaultdict(int)

        required = len(cnts)
        formed = 0

        ans = ""
        while right < N:
            ch = s[right]
            window_cnts[ch] += 1

            if ch in cnts and window_cnts[ch] == cnts[ch]:
                formed += 1

            while formed == required:
                cur_len = right-left+1
                if cur_len < min_len:
                    min_len = cur_len
                    ans = s[left:right+1]

                window_cnts[s[left]] -= 1

                if s[left] in cnts and window_cnts[s[left]] < cnts[s[left]]:
                    formed -= 1
                left += 1      
            
            right += 1

        return ans    