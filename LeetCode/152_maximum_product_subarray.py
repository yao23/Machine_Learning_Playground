class Solution(object):
    # beats 20.16%
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        max[i] = max(nums[i], nums[i] * max[i - 1], nums[i] * min[i - 1])
        min[i] = min(nums[i], nums[i] * max[i - 1], nums[i] * min[i - 1])

        time: O(n), space: O(1)
        """
        min_tmp = nums[0]
        max_tmp = nums[0]
        max_res = nums[0]
        for i in xrange(1, len(nums)):
            min_tmp, max_tmp = min(nums[i], nums[i] * max_tmp, nums[i] * min_tmp), max(nums[i], nums[i] * max_tmp,
                                                                                       nums[i] * min_tmp)
            max_res = max(max_res, max_tmp)
        return max_res
