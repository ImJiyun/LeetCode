class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        alpha_idxes = {}

        for i, c in enumerate(s):
            if not c in alpha_idxes:
                alpha_idxes[c] = [i, i]
            else:
                alpha_idxes[c][1] = i

        arr = list(alpha_idxes.values()) 
        arr.sort(key=lambda x: x[0])

        left, right = arr[0][0], arr[0][1]
        ans = []
        print(arr)
        for num1, num2 in arr:
            if num1 > right:
                ans.append(right-left+1)
                left, right = num1, num2
            elif num2 > right:
                right = num2    

        ans.append(right - left + 1)
        
        return ans