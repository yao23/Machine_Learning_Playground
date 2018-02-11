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

        beats 83.95%
        """
        count = 0
        num_dict = {}
        for i in C:
            for j in D:
                s = i + j
                if s in num_dict:
                    num_dict[s] += 1
                else:
                    num_dict[s] = 1

        for i in range(len(A)):
            for j in range(len(B)):
                target = 0 - (A[i] + B[j])
                if target in num_dict:
                    count += num_dict[target]
        return count

    def fourSumCount1(self, A, B, C, D):
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
