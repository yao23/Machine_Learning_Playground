class Solution(object):
    # beats 94.38%
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        iniArr = [0]
        if num > 0:
            amountToAdd = 1
            while len(iniArr) < num + 1:
                iniArr.extend([x + 1 for x in iniArr])

        return iniArr[0:num + 1]