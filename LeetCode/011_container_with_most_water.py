class Solution(object):
    # beats 97.39%
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res

    # https://discuss.leetcode.com/topic/14940/simple-and-clear-proof-explanation
    def maxArea1(self, height):
        # beats 46.59%
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water

    # https://discuss.leetcode.com/topic/16754/simple-and-fast-c-c-with-explanation
    def maxArea2(self, height):
        # beats 81.42%
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            h = min(height[left], height[right])
            water = max(water, h * (right - left))
            while height[left] <= h and left < right:
                left += 1
            while height[right] <= h and left < right:
                right -= 1
        return water
