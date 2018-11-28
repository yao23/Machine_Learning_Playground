class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]

        beats 18.26%
        """
        res = [0] * (length + 1)
        for u in updates:
            res[u[0]] += u[2]
            res[u[1]+1] -= u[2]
        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        res.pop()
        return res
