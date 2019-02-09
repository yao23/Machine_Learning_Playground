class Solution(object):
    def search(self, nums, target):
        """
        :param nums:
        :param target:
        :return:

        https://discuss.leetcode.com/topic/13096/python-binary-search-solution-o-logn-48ms
        beats 98.63%
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        https://discuss.leetcode.com/topic/34467/pretty-short-c-java-ruby-python/2
        beats 28.80%
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                low = mid + 1
            else:
                high = mid
        return low if target in nums[low:low + 1] else -1
