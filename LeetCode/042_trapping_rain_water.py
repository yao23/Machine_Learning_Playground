class Solution(object):
    # @param {integer[]} height
    # @return {integer}
    # beats 86.48%
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right, water, min_height = 0, n - 1, 0, 0
        while left < right:
            while left < right and height[left] <= min_height:
                water += (min_height - height[left])
                left += 1
            while right > left and height[right] <= min_height:
                water += (min_height - height[right])
                right -= 1
            min_height = min(height[left], height[right])
        return water
