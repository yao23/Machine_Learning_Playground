class Solution(object):
    def isPerfectSquare(self, num: int) -> bool:
        """
        https://www.youtube.com/watch?v=Cg_wWPHJ2Sk&list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&index=3
        
        beats 96.54%
        """
        l, r = 1, num
        while l <= r:
            m = (l + r) // 2
            sq = m * m
            if sq > num:
                r = m - 1
            elif sq < num:
                l = m + 1
            else:
                return True
        return False
    
    def isPerfectSquare1(self, num: int) -> bool:
        """
        https://www.youtube.com/watch?v=Cg_wWPHJ2Sk&list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&index=3
        
        beats 5.48%
        """
        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
    
    def isPerfectSquare0(self, num):
        """
        :type num: int
        :rtype: bool

        beats 15.65%
        """
        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num
