class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        gas = [3, 4, 3, 6, 7, 1, 2]
        cost = [2, 4, 5, 1, 5, 1, 3]
        start = 4 (gas[4] = 7, cost[4] = 5)

        beats 18.86%
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

    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        beats 73.08%
        """
        len_gas = len(gas)
        len_cost = len(cost)
        if len_gas == 0 or len_cost == 0 or sum(gas) < sum(cost):
            return -1

        start = len_gas - 1
        end = 0
        gas_left = (gas[start] - cost[start])
        while end < start:
            if gas_left < 0:  # need more gas in start
                start -= 1
                gas_left += (gas[start] - cost[start])
            else:  # continue
                gas_left += (gas[end] - cost[end])
                end += 1
        if gas_left >= 0:
            return start
        else:
            return -1
