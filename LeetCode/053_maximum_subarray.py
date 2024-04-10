class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=5WZl3MMT0Eg

        beats 67.36%
        """
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
    
    def maxSubArrayV1(self, nums: List[int]) -> int:
        """
        beats 54.64%
        """
        res = float("-inf")
        curSum = 0
        for n in nums:
            if curSum + n < 0:
                curSum = 0
                res = max(res, n)
            else:
                curSum += n
                res = max(res, curSum)
        return res
        
    def maxSubArrayV0(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        only non-negative number contribute to the maximum sub-array

        beats 78.72%
        """
        if not nums:
            return 0

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
