class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=4v42XOuU1XA&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=31
        
        DP

        beats 60.05%
        """
        sumEven, sumOdd = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tmpEven, tmpOdd

        return sumEven
        
    def maxAlternatingSumV0(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=4v42XOuU1XA&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=31

        dfs / backtracking with memorization
        
        beats 7.77%
        """
        dp = {}

        def dfs(i, even): # i - index, even - true (+) / odd (-) - false
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]
            total = nums[i] if even else (-1 * nums[i])
            dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even)) # max of use nums[i] or not
            return dp[(i, even)]

        return dfs(0, True)
