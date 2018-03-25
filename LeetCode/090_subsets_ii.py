class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        # if S[i] is same to S[i - 1], then it needn't to be added to all of the subset,
        # just add it to the last l subsets which are created by adding S[i - 1]
        # @param num, a list of integer
        # @return a list of lists of integer
        # beats 96.66%
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
