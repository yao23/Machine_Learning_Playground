import random


class Solution(object):
    """
    https://leetcode.com/problems/random-pick-index/discuss/88069/Simple-Python-solution

    beats 70.84%
    """
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([k for k, v in enumerate(self.nums) if v == target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
