class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        beats 65.04%
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True

    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        beats 49.12%
        """
        return reduce(lambda m, (i, n): max(m, i + n) * (i <= m), enumerate(nums, 1), 1) > 0

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        beats 98.78%
        """
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
