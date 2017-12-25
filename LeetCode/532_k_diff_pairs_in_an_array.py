import math


class Solution:
    # [3, 1, 4, 1, 5], k = 2 => 2 ((1,3), (3,5))
    # [1, 2, 3, 4, 5], k = 1 => 4 ((1, 2), (2, 3), (3, 4), (4, 5))
    # [1, 3, 1, 5, 4], k = 0 => 1 (1,1)
    # [1,1,1,1,1], k = 0 => 1 (1,1)
    # beats 26.83%
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_len = len(nums)
        if num_len < 2:
            return 0
        if k < 0:
            return 0

        left = 0
        right = 1
        count = 0
        k = math.fabs(k)
        nums = sorted(nums)
        while right < num_len:
            if left >= right or nums[right] - nums[left] < k:
                right += 1
            elif left > 0 and nums[left - 1] == nums[left] or nums[right] - nums[left] > k:  # skip left duplicates
                left += 1
            else:
                right += 1
                count += 1
                while right < num_len and nums[right - 1] == nums[right]:  # skip right duplicates
                    right += 1
        return count
