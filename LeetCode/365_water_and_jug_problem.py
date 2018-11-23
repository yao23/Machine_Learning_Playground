class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool

        beats 16.42%
        """
        from fractions import gcd
        return z == 0 or x + y >= z and z % gcd(x, y) == 0
