class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int

        https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
        https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22+-*%22-completely-bit-manipulation-guaranteed

        https://leetcode.com/problems/sum-of-two-integers/discuss/84290/Java-simple-easy-understand-solution-with-explanation

        beats 29.67%
        """
        # 32 bits integer max
        max_int = 0x7FFFFFFF
        # 32 bits interger min
        min_int = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= max_int else ~(a ^ mask)
