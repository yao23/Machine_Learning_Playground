class Solution(object):
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        https://www.youtube.com/watch?v=dw2nMCxG0ik&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=27
        
        beats 35.19%
        """
        dp = {0 : 1} # k - target, v - num of combinations
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums: # dp[4] = dp[3] + dp[2] + dp[1]
                dp[total] += dp.get(total - n, 0)
        return dp[target]
        
    def combinationSum4V0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        beats 87.90%
        """
        nums, combs = sorted(nums), [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    combs[i] += 1
                if num < i:
                    combs[i] += combs[i - num]
        return combs[target]
