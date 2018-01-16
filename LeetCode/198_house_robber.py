class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        money list: [m0,m1,m2,m3,...]
        [m0], max = mo
        [m0,m1], max = Max(m0, m1)
        [m0,m1,m2], max = Max(m0 + m2, m1)

        f(0) = nums[0]
        f(1) = max(num[0], num[1])
        f(k) = max( f(k-2) + nums[k], f(k-1) )

        beats 87.64%
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
