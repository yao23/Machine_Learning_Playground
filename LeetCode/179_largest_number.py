class Solution:
    """
    @param {integer[]} nums
    @return {string}

    The actual sort procedure is done by Python, the cpm just let Python know how to compare the them.
    For example, if you compare '3' and '30', then the cpm will try to compare '330' and '303', then it'll decide 3 is
    bigger than 30 because '330' is bigger than '303'.

    https://leetcode.com/problems/largest-number/discuss/53270/
    https://leetcode.com/problems/largest-number/discuss/53162/

    beats 91.37%
    """
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(nums).lstrip('0') or '0'
