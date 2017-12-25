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

    # beats 73.08%
    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
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
