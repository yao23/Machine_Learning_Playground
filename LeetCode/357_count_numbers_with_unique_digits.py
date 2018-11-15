class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int

        beats 90.53%
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product

        return ans
