class Solution(object):
    # The stack maintain the indexes of buildings with ascending height (h time broader width w will result in bigger
    # area). Before adding a new building pop the building who is taller than the new one. The building popped out
    # represent the height of a rectangle with the new building as the right boundary and the current stack top as the
    # left boundary. Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.
    # beats 39.11%
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans
