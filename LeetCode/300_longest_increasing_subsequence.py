class Solution(object):
    # beats 82.38%
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/
        https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

        tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
        For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:
        len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
        len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
        len = 3   :      [4, 5, 6]            => tails[2] = 6

        We can easily prove that tails is a increasing array.
        Therefore it is possible to do a binary search in tails array to find the one needs update.
        Each time we only do one of the two:
        (1) if x is larger than all tails, append it, increase the size by 1
        (2) if tails[i-1] < x <= tails[i], update tails[i]
        Doing so will maintain the tails invariant. The the final answer is just the size.

        """
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            left, right = 0, size
            while left != right:
                mid = (left + right) / 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
            size = max(left + 1, size)
        return size
