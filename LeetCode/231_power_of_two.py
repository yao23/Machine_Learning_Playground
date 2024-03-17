class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        """
        https://www.youtube.com/watch?v=H2bjttEV4Vc
        
        beats 50.42%
        """
        x = 1
        while x < n:
            x *= 2
        return x == n
        
    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool

        beats 9.48%
        """
        return n > 0 and not (n & n-1)

    def isPowerOfTwo0(self, n: int) -> bool:
        """
        https://www.youtube.com/watch?v=H2bjttEV4Vc

        beats 24.42%
        """
        return n > 0 and ((1 << 30) % n == 0)
