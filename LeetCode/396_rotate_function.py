class Solution(object):
    # beats 8.00%
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        totalSum = sum(A)
        lMax = 0
        for i in range(len(A)):
            lMax += i * A[i]
        gMax = lMax
        for i in range(len(A)-1, 0, -1):
            lMax += (totalSum - A[i] * len(A))
            gMax = max(gMax, lMax)
        return gMax