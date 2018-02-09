class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/find-the-duplicate-number/discuss/73022/Python-Solution-with-O(1)-space-and-O(nlogn)-time

        The difficulty in this problem lies in O(1) space, and many solution using O(n) space can also be accepted by OJ.
        The solution is applying bi-search in the range[1, n] by counting the element which falls in sub range(n/2, n].
        If the number is bigger than capacity of that sub range, it means the duplicated integer falls in the sub-range.
        Otherwise the duplicated integer falls in the other half sub range.

        beats 19.30%
        """
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k <= high:  # right half
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return high
