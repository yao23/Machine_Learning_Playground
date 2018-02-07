class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        beats 86.48%

        https://discuss.leetcode.com/topic/5125/sharing-my-simple-c-code-o-n-time-o-1-space
        https://discuss.leetcode.com/topic/18720/8-lines-c-c-java-python-solution/3

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

    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int

        each height only contribute when it's shorter than min of left max and right max heights
        the contribution is difference between current height and min(left_max, right_max)

        time:O(n), space:O(n)

        beats 60.76%
        """
        n = len(height)
        left_max = right_max = 0
        l_max_arr = [0] * n
        r_max_arr = [0] * n
        for i in range(n):  # find left max for every element
            l_max_arr[i] = left_max
            if height[i] > left_max:
                left_max = height[i]
        for i in range(n - 1, -1, -1):  # find right max for every element
            r_max_arr[i] = right_max
            if height[i] > right_max:
                right_max = height[i]

        water = 0
        for i, h in enumerate(height):
            min_height = min(l_max_arr[i], r_max_arr[i])
            if h < min_height:  # difference between min_height and current height
                water += (min_height - h)
        return water
