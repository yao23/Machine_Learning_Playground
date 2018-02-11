class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/valid-triangle-number/discuss/104164/Can-this-problem-possibly-be-solved-by-python

        beats 64.31%
        """
        ans = 0
        nums.sort()
        for i in range(2, len(nums)):
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    ans += end - start
                    end -= 1
                else:
                    start += 1
        return ans

    def triangleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/valid-triangle-number/discuss/104187/Python-O(n2)-solution-526-ms

        beats 27.14%
        """
        nums = sorted(nums)
        total = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            end = i + 2
            for j in range(i + 1, len(nums) - 1):
                while end < len(nums) and nums[end] < (nums[i] + nums[j]):
                    end += 1
                total += end - j - 1
        return total