class Solution(object):
    # beats 82.34%
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float('inf')
        profit = 0
        for i in prices:
            profit = max(profit, i-low)
            low = min(low, i)
        return profit