class Solution(object):
    # beats 75.53%
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        highDigit = 1
        while highDigit * 10 <= n:
            highDigit *= 10
        higherDigit = highDigit * 10
        withKeys = []
        for i in xrange(1, n+1):
            key = i
            while key < highDigit:
                key *= 10
            withKeys.append(key * higherDigit + i)
        withKeys.sort()
        return [ki % higherDigit for ki in withKeys]