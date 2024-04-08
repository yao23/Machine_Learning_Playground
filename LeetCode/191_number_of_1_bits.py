class Solution(object):
    def hammingWeight(self, n: int) -> int:
        """
        https://www.youtube.com/watch?v=5Km3utixwZs
        
        beats 83.70%
        """
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1 # same as n // 2
        return count
        
    def hammingWeightV0(self, n):
        """
        :type n: int
        :rtype: int

        beats 57.20%
        """
        return bin(n).count('1')

    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int

        beats 57.20%
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
