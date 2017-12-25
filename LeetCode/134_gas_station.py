class Solution(object):
    # beats 18.86%
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0  # current tank balance
        for i in range(len(gas)):
            balance += (gas[i] - cost[i])  # update balance
            if balance < 0:  # balance drops to negative, reset the start position
                balance = 0
                position = (i + 1)
        return position
