class Solution(object):
    # beats 19.30%
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return high