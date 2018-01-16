class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        beats 57.04%
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        it allows trade as many transactions as possible to maximize profit,
        if later prices is higher than previous one, it could generate profit and make trade
        when buy previous one and sell later one, finally return accumulated sum

        beats 77.26%
        """
        len_prices = len(prices)
        if len_prices == 0:
            return 0
        else:
            max_profit = 0
            for i in range(len_prices - 1):
                if prices[i + 1] > prices[i]:
                    max_profit += (prices[i + 1] - prices[i])
            return max_profit
