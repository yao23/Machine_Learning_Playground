class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int

        beats 27.91%
        """
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q /= 10
            ans += q * x
            if digit == 1:
                ans += n % x + 1
            elif digit > 1:
                ans += x
            x *= 10
        return ans
