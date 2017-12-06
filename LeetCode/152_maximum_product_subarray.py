class Solution(object):
    # beats 20.16%
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MinTemp = nums[0]
        MaxTemp = nums[0]
        Max = nums[0]
        for i in xrange(1, len(nums)):
            MinTemp, MaxTemp = min(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp), max(nums[i], nums[i] * MaxTemp,
                                                                                       nums[i] * MinTemp)
            Max = max(Max, MaxTemp)
        return Max