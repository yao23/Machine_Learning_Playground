class Solution(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        https://www.youtube.com/watch?v=ypn0aZ0nrL4

        beats 22.75%
        """
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

    def containsNearbyDuplicateV0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        beats 15.63%
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
