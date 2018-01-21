class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        the largest width is from start to end
        later heights can compete only with larger heights, so move smaller between left and right heights

        beats 97.39%
        """
        left, right, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[left] < height[right]:
                res, left = max(res, height[left] * w), left + 1
            else:
                res, right = max(res, height[right] * w), right - 1
        return res

    def maxArea1(self, height):
        """
        :param height:
        :return:

        https://discuss.leetcode.com/topic/14940/simple-and-clear-proof-explanation

        the largest width is from start to end
        later heights can compete only with larger heights, so move smaller between left and right heights

        beats 46.59%
        """
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

    def maxArea2(self, height):
        """
        :param height:
        :return:

        https://discuss.leetcode.com/topic/16754/simple-and-fast-c-c-with-explanation

        the largest width is from start to end
        later heights can compete only with larger heights, so move left and right heights until meet larger ones

        beats 81.42%
        """
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
