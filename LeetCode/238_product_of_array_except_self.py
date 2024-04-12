class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://www.youtube.com/watch?v=bNvIQI2wAjk
        
        beats 22.67%
        """
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        beats 95.35%
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
