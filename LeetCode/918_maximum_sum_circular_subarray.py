class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=fxT9KjakYPM

        beats 33.26%
        """
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        totalSum = 0
        for n in nums:
            totalSum += n
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)

        return max(globalMax, totalSum - globalMin) if globalMax > 0 else globalMax
        # if globalMax <= 0, which means all zeor or negative number, globalMax is the result as totalSum equals globalMin
