class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        left_max_height, right_max_height = 0, 0
        left_max_heights = [0] * N
        right_max_heights = [0] * N

        for i in range(N):
            left_max_height = max(left_max_height, height[i])
            left_max_heights[i] = left_max_height

        for i in range(N-1, -1, -1):
            right_max_height = max(right_max_height, height[i])
            right_max_heights[i] = right_max_height

        heights = [0] * N

        for i in range(N):
            heights[i] = min(left_max_heights[i], right_max_heights[i])

        rain = 0

        for i in range(N):
            rain += heights[i] - height[i]

        return rain