class Solution(object):
    # https://discuss.leetcode.com/topic/34467/pretty-short-c-java-ruby-python/2
    # beats 28.80%
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                low = mid + 1
            else:
                high = mid
        return low if target in nums[low:low + 1] else -1
