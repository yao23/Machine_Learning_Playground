class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        brute force:
        it's not hard to come out the idea to get differences between any 2 days,
        and get max profit by add two appropriate differences in O(n^2)

        optimization:
        the goal is to speed up to O(n)
        the idea is based on brute force (two appropriate differences are previous max profit and later one)
        and Buy and Sell Stock I (get max profit in O(n) with one pass forward and another pass backward)

        beats 70.83%
        """
        if not prices:
            return 0

        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max
