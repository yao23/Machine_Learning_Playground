import random


class Solution(object):
    """
    https://leetcode.com/problems/shuffle-an-array/discuss/85957/easy-python-solution-based-on-generating-random-index-and-swapping

    generating random index and swapping

    beats 58.33%
    """

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans


class Solution1(object):
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


class Solution2(object):
    """
    https://leetcode.com/problems/shuffle-an-array/discuss/86000/Python.-Solution-in-a-few-lines

    beats 31.94%
    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self._array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled_array = self._array[:]
        random.shuffle(shuffled_array)
        return shuffled_array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
