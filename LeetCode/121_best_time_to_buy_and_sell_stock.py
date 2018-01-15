class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        find min difference between later element and previous one

        find min element before current one (store in an array, then optimize as a tmp variable (low)

        update max profit with difference between previous min and current one

        beats 82.34%
        """
        low = float('inf')
        profit = 0
        for i in prices:
            profit = max(profit, i-low)
            low = min(low, i)
        return profit
