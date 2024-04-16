class Solution:
    """
    https://www.youtube.com/watch?v=gdXkkmzvR3c
    
    beats 25.85%
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = ceil(totalSum / 2) # 23 => 12, 24 => 12, try to split stones to 2 even halves for smallest weight
        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (totalSum - total)) # 12 - (23 - 12) = 12 - 11 = 1, absolute value when total < target and i == len(stones)
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(
                dfs(i + 1, total), # not take current stone
                dfs(i + 1, total + stones[i]), # take current stone
            )
            return dp[(i, total)]

        return dfs(0, 0)
