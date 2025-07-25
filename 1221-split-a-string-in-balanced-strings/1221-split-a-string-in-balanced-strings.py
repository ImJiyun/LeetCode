class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {"R" : 0, "L": 0}

        N = len(s)
        ans = 0

        for i in range(N):
            cnt[s[i]] += 1
            if cnt['R'] == cnt['L']:
                ans += 1
                cnt = {"R" : 0, "L": 0}

        return ans        