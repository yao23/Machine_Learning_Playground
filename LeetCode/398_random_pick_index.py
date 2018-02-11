import random
from random import random


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


class Solution2(object):
    """
    https://leetcode.com/problems/random-pick-index/discuss/88081/Python-solution-with-detailed-explanation

    Do we want to optimize run time or memory? If we want to optimize run time then we can use a dictionary to
    pre-process the nums array. Simply create a map of key (number) and value (list of its indices). Then run reservoir
    sampling over this input.

    But the problem statement says that using too much memory is not allowed. In that case, we can iterate the entire
    array and keep a variable to track the frequency of the target for input into reservoir sampling.

    Notice random() returns uniform random number between [0 to 1]

    beats 91.30%
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
        cnt, index = 0, 0
        for idx, x in enumerate(self.nums):
            if x == target:
                cnt += 1
                if random() <= 1.0/(cnt):
                    index = idx
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
