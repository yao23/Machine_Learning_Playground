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


class Solution1(object):
    """
    https://leetcode.com/problems/random-pick-index/discuss/88153/Python-reservoir-sampling-solution.

    reservoir sampling

    beast 46.55%
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
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
