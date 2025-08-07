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

        def check():
            for ch in cnts:
                if window_cnts[ch] < cnts[ch]:
                    return False
            print(window_cnts)        
            return True

        ans = ""
        while right < N:
            window_cnts[s[right]] += 1

            while check():
                cur_len = right-left+1

                if cur_len < min_len:
                    min_len = cur_len
                    ans = s[left: right+1]

                window_cnts[s[left]] -= 1
                left += 1
            
            right += 1

        return ans    