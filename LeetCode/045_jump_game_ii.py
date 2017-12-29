class Solution(object):
    # @param {integer[]} nums
    # @return {integer}
    # beats 44.25%
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            max_end = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end
        return step
