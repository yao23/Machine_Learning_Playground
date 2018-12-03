from itertools import groupby


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        beats 44.44%
        """
        norep = [num for num, _ in groupby(nums)]
        triples = zip(norep, norep[1:], norep[2:])
        return sum((b>a) == (b>c) for a, b, c in triples) + len(norep[:2])

    def wiggleMaxLength1(self, nums):
        """
        :param nums:
        :return:

        beats 97.22%
        """
        norep = [num for num, _ in groupby(nums)]
        if len(norep) < 2: return len(norep)
        triples = zip(norep, norep[1:], norep[2:])
        return 2 + sum(a < b > c or a > b < c for a, b, c in triples)
