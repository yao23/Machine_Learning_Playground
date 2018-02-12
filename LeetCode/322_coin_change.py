class Solution(object):
    """
    This solution is inspired by the BFS solution for problem Perfect Square.
    Since it is to find the least coin solution (like a shortest path from 0 to amount),
    using BFS gives results much faster than DP.
    https://discuss.leetcode.com/topic/26262/short-python-solution-using-bfs

    beats 97.75%
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        cur_queue = [0]  # current queue
        next_queue = []  # next queue
        num_counter = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while cur_queue:
            num_counter += 1
            for v in cur_queue:
                for coin in coins:
                    new_val = v + coin
                    if new_val == amount:
                        return num_counter
                    elif new_val > amount:
                        continue
                    elif not visited[new_val]:
                        visited[new_val] = True
                        next_queue.append(new_val)
            cur_queue, next_queue = next_queue, []
        return -1

    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins,
        dp[i] = min(dp[i - coin] + 1).
        dp[i] works as a cache, max_val is default value, otherwise is cached

        The time complexity is O(amount * coins.length) and the space complexity is O(amount)

        [dp[amount], -1][dp[amount] == max_val] => [dp[amount], -1][0/1]
        if dp[amount] == max_val: [dp[amount], -1][1] => -1
        else: [dp[amount], -1][0] => dp[amount]

        https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code

        beats 77.61%
        """
        max_val = float('inf')
        dp = [0] + [int(max_val)] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else max_val for c in coins]) + 1

        # return [dp[amount], -1][dp[amount] == max_val]

        if dp[amount] == max_val:
            return -1
        else:
            return dp[amount]

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        brute force

        Time Limit Exceeded (TLE)
        """
        if coins is None or amount < 0:
            return -1
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        if amount < coins[-1]:
            return -1
        return self.help_func(coins, amount, 0, [])

    def help_func(self, coins, amount, depth, res_list):
        """
        :param coins:
        :param amount:
        :param depth:
        :param res_list:
        :return:

        use current largest coin as much as possible
        back tracking to use less largest coin if cannot make the target amount
        repeat above procedure for each coin from large to small
        """
        coins_len = len(coins)
        if depth == coins_len:
            return -1
        if amount == 0:
            return len(res_list)
        elif amount < 0:
            return -1
        else:
            i = depth
            coin_nums = amount // coins[i]
            for cur_coin_num in range(coin_nums, -1, -1):
                cur_amount = amount - coins[i] * cur_coin_num
                tmp_res = self.help_func(coins, cur_amount, depth + 1, res_list + [coins[i]] * cur_coin_num)
                if tmp_res == -1:
                    continue
                else:
                    return tmp_res
            return -1

    def coinChange3(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        BFS with explanation

        """
        # if coins is None or amount < 0:
        #     return -1
        # if amount == 0:
        #     return 0
        # coins.sort(reverse=True)
        # if amount < coins[-1]:
        #     return -1
        cur_queue = coins
        min_nums = [0] * (amount + 1)  # min num to make amount
        for coin in coins:
            if coin <= amount:
                min_nums[coin] = 1
                if coin == amount:
                    return min_nums[coin]
        num = 1
        while cur_queue:
            next_queue = []
            all_larger_amount = True
            for cur_amount in cur_queue:
                for coin in coins:
                    total_amount = cur_amount + coin
                    if total_amount <= amount and min_nums[total_amount] == 0:
                        min_nums[total_amount] = num
                        all_larger_amount = False
                        if total_amount == amount:
                            return min_nums[total_amount] + 1
                    if total_amount not in next_queue:
                        next_queue.append(total_amount)
            if all_larger_amount:
                return -1
            else:
                cur_queue = list(next_queue)
                num += 1
        return -1
