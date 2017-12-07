# This solution is inspired by the BFS solution for problem Perfect Square.
# Since it is to find the least coin solution (like a shortest path from 0 to amount),
# using BFS gives results much faster than DP.
# https://discuss.leetcode.com/topic/26262/short-python-solution-using-bfs

class Solution(object):
    # beats 97.75%
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1