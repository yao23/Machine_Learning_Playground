class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            mNum = nums[mid]
            if mNum == target:
                return mid
            elif mNum < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
