import math


class Solution:
    # beats 8.33%
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters)
        house_num = len(houses)
        heater_num = len(heaters)
        house_index = 0
        heater_index = 0
        res = 0

        while house_index < house_num:
            while (heater_index < heater_num - 1) and (
                    math.fabs(heaters[heater_index + 1] - houses[house_index]) <= math.fabs(
                    heaters[heater_index] - houses[house_index])):
                heater_index += 1
            res = max(res, int(math.fabs(heaters[heater_index] - houses[house_index])))
            house_index += 1

        return res
