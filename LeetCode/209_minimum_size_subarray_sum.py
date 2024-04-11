class Solution(object):
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=aYqYMIqZx5s

        beats 72.90%
        """
        res = float('inf')
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float('inf') else 0
        
    def minSubArrayLenV0(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

        beats 85.23%
        """
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
