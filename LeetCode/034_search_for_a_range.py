class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        @param A, a list of integers
        @param target, an integer to be searched
        @return a list of length 2, [index1, index2]
        beats 39.47%
        """
        start = self.binary_search(nums, target-0.5)
        if not target in nums[start:start+1]:
            return [-1, -1]
        nums.append(0)
        end = self.binary_search(nums, target+0.5)-1
        return [start, end]

    def binary_search(self, arr, target):
        start, end = 0, len(arr)-1
        while start < end:
            mid = (start+end)//2
            if target < arr[mid]:
                end = mid
            else:
                start = mid+1
        return start
