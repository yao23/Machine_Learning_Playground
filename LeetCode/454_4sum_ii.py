import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int

        https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python

        beats 33.83%
        """
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
