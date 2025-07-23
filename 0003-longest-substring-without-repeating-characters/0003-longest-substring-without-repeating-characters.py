class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_set = set()
        left, right = 0, 0
        longest = 0

        while right < len(s):
            while s[right] in str_set:
                str_set.remove(s[left])
                left += 1
            longest = max(longest, right-left+1)
            str_set.add(s[right])
            right += 1

        return longest