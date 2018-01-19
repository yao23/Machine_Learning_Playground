class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        major is always in middle index after sort the input array

        beats 89.88%
        """
        return sorted(nums)[len(nums)/2]

    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/majority-element/discuss/51613/
        if current element is equal to major then contribute to the counter
        otherwise it should decrease the counter
        when counter is zero, it means a new major number start

        beats 51.59%
        """
        len_nums = len(nums)
        major = nums[0]
        count = 1
        for i in range(1, len_nums):
            if count == 0:
                major = nums[i]
                count = 1
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
