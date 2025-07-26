class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []

        def dfs(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    ans.append(".".join(parts))
                    return

            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start: start + length]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                dfs(start+length, parts + [part])
        dfs(0, [])
        return ans