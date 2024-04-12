class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=u89i60lYx8U
        
        beats 25.15%
        """
        total = sum(nums)  # O(n)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

    def pivotIndexV0(self, nums: List[int]) -> int:
        """
        beats 25.15%
        """
        length = len(nums)
        if length == 0:
            return -1
        elif length == 1:
            return 0

        preSum = [0] # preSum: sum from first to current
        for n in nums:
            preSum.append(n + preSum[-1])
        
        if preSum[1] == preSum[-1]: # first is pivot (left and right are zero)
            return 0
        
        for i in range(1, length):
            if preSum[i - 1] == preSum[-1] - preSum[i]: # left equals right
                return i - 1

        if preSum[-2] == 0: # last is pivot
            return length - 1

        return -1
