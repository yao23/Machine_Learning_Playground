class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        beats 68.70%
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
