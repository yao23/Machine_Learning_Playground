class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        
        beats 35.60%
        """
        n = len(prices)
        if n < 2:
            return 0
        # k is big enough to cover all ramps.
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        global_max = [[0] * n for _ in xrange(k + 1)]
        for i in xrange(1, k + 1):
            # The max profit with i transactions and selling stock on day j.
            local_max = [0] * n
            for j in xrange(1, n):
                profit = prices[j] - prices[j - 1]
                local_max[j] = max(
                    # We have made max profit with (i - 1) transactions in
                    # (j - 1) days.
                    # For the last transaction, we buy stock on day (j - 1)
                    # and sell it on day j.
                    global_max[i - 1][j - 1] + profit,
                    # We have made max profit with (i - 1) transactions in
                    # (j - 1) days.
                    # For the last transaction, we buy stock on day j and
                    # sell it on the same day, so we have 0 profit, apparently
                    # we do not have to add it.
                    global_max[i - 1][j - 1],  # + 0,
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1) sale and sell it on
                    # day j.
                    local_max[j - 1] + profit)
                global_max[i][j] = max(global_max[i][j - 1], local_max[j])
        return global_max[k][-1]

    def maxProfit1(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int

        beats 50.00%
        """
        if not prices:
            return 0

        n = len(prices)
        if k >= n // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)

        profits = [0] * n
        for j in range(k):
            # Update new_profits
            max_all = max_prev = max_here = 0
            for i in range(1, n):
                profit = prices[i] - prices[i - 1]
                max_here = max(max_here + profit, max_prev + profit, max_prev)
                max_prev = profits[i]
                profits[i] = max_all = max(max_all, max_here)
        return profits[-1]

    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int

        beats 88.10%
        """
        n = len(prices)
        if n == 0:
            return 0
        if k > n // 2:
            return sum(i - j
                       for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        memo = [0] * n
        for i in range(k):
            tmp_memo = [0]
            cur_max, tmp_max = -prices[0], 0
            for j in range(1, n):
                if cur_max + prices[j] > tmp_max:
                    tmp_max = cur_max + prices[j]
                    tmp_memo.append(tmp_max)
                else:
                    tmp_memo.append(tmp_max)
                if memo[j - 1] - prices[j] > cur_max:
                    cur_max = memo[j - 1] - prices[j]
            memo = tmp_memo

        return memo[-1]
