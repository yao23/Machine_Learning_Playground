class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        beats 89.17%
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        to_check = {n}
        while to_check:
            cnt += 1
            temp = set()
            for x in to_check:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            to_check = temp

        return cnt
