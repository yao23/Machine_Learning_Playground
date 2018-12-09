class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]

        beats 75.53%
        """
        high_digit = 1
        while high_digit * 10 <= n:
            high_digit *= 10
        higher_digit = high_digit * 10
        with_keys = []
        for i in xrange(1, n+1):
            key = i
            while key < high_digit:
                key *= 10
            with_keys.append(key * higher_digit + i)
        with_keys.sort()
        return [ki % higher_digit for ki in with_keys]
