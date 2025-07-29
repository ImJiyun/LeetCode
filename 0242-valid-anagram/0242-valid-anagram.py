from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnts = defaultdict(int)

        for ch in s:
            cnts[ch] += 1

        for ch in t:
            if cnts[ch] > 0:
                cnts[ch] -= 1
                if cnts[ch] == 0:
                    del cnts[ch]
            else:
                return False
        
        return len(cnts) == 0                