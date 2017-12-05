from itertools import groupby

class Solution(object):
    # beats 44.44%
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        norep = [num for num, _ in groupby(nums)]
        triples = zip(norep, norep[1:], norep[2:])
        return sum((b>a) == (b>c) for a, b, c in triples) + len(norep[:2])

    # beats 97.22%
    def wiggleMaxLength1(self, nums):
        norep = [num for num, _ in groupby(nums)]
        if len(norep) < 2: return len(norep)
        triples = zip(norep, norep[1:], norep[2:])
        return 2 + sum(a < b > c or a > b < c for a, b, c in triples)