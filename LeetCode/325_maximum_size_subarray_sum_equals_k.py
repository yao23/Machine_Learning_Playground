class Solution(object):
    # beats 33.69%
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, acc = 0, 0  # answer and the accumulative value of nums
        mp = {0: -1}  # key is acc value, and value is the index
        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i
            if acc - k in mp:
                ans = max(ans, i - mp[acc - k])
        return ans