class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

        beats 70.33%
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]:  # tricky part
                left += 1
            # the first half is ordered
            if nums[left] <= nums[mid]:
                # target is in the first half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
