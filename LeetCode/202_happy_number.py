class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool

        beats 40.96%
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

    def isHappy1(self, n):
        """
        :type n: int
        :rtype: bool

        https://leetcode.com/problems/happy-number/discuss/56915/
        endless cycle means has some replication (repeated number) when calculate square sum for each digit

        beats 54.70%
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
