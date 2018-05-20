class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]

        beats 27.01%
        """
        result = []
        nums.append(upper+1)
        pre = lower - 1
        for i in nums:
            if i == pre + 2:
                result.append(str(i-1))
            elif i > pre + 2:
                result.append(str(pre + 1) + "->" + str(i -1))
            pre = i
        return result
