import random


class Solution(object):
    """
    https://leetcode.com/problems/shuffle-an-array/discuss/86053/Python-hack

    beats 33.10%
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
