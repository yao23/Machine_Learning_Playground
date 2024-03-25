class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        https://www.youtube.com/watch?v=IsvocB5BJhw&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=31
        
        beats 88.81%
        """
        total = sum(nums)
        if total % 2:
            return False

        dp = set()
        dp.add(0)

        target = total // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                tmp = t + nums[i]
                if tmp == target:
                    return True
                nextDP.add(tmp) # add cur num
                nextDP.add(t) # no cur num
            dp = nextDP
        return True if target in dp else False

    def canPartitionV0(self, nums: List[int]) -> bool:
        """
        beats 10.54%
        """
        dp = {}
        total = 0
        for i, n in enumerate(nums):
            total += n

        if total % 2: # total sum is odd
            return False

        def dfs(i, sum):
            if i == len(nums):
                return False
            if (i, sum) in dp:
                return dp[(i, sum)]
            if sum == total // 2: # sum is half of total sum
                return True
            dp[(i, sum)] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum) # either use nums[i] or not
            return dp[(i, sum)]

        return dfs(0, 0)
