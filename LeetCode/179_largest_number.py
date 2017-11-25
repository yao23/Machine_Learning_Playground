class Solution:
    # @param {integer[]} nums
    # @return {string}

    # beats 91.37%
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(nums).lstrip('0') or '0'