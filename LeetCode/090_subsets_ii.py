class Solution(object):
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        https://www.youtube.com/watch?v=Vn2v6ajA7U0
        
        beats 39.49%
        """
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
    
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
                length = len(res)
            for j in range(len(res) - length, len(res)):
                res.append(res[j] + [nums[i]])
        return res
