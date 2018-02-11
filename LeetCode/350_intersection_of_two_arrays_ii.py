import collections
from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        beats 75.88%
        """
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

    def intersect1(self, nums1, nums2):
        C = collections.Counter
        return list((C(nums1) & C(nums2)).elements())

    def intersect2(self, nums1, nums2):
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

    def intersect3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82373/A-dictionary-based-solution-in-python

        beats 75.88%
        """
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        ret = []
        for i in nums2:
            if i in dict1 and dict1[i] > 0:
                ret.append(i)
                dict1[i] -= 1
        return ret

    def intersect4(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions

        beats 60.14%
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res