class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
