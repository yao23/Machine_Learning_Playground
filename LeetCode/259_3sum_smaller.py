class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        https://discuss.leetcode.com/topic/42006/why-is-sorting-allowed/3
        beats 88.46%
        """
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
        return count
