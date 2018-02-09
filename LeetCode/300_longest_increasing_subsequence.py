class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/
        https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

        tails is an array storing the smallest tail of all increasing sub-sequences with length i+1 in tails[i].
        For example, say we have nums = [4,5,6,3], then all the available increasing sub-sequences are:
        len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
        len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
        len = 3   :      [4, 5, 6]            => tails[2] = 6

        We can easily prove that tails is a increasing array.
        Therefore it is possible to do a binary search in tails array to find the one needs update.
        Each time we only do one of the two:
        (1) if x is larger than all tails, append it, increase the size by 1
        (2) if tails[i-1] < x <= tails[i], update tails[i]
        Doing so will maintain the tails invariant. The the final answer is just the size.

        beats 82.38%

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

    def lengthOfLIS1(self, nums):
        """
        :param nums:
        :return:

        insertion sort similar idea to find longest increasing sequence

        beats 72.99%
        """
        nums_len = len(nums)
        result = [1] * nums_len
        res_len = 0
        for i in range(nums_len):
            start = 0
            end = res_len
            while start < end - 1:
                mid = start + (end - start) // 2
                if result[mid] < nums[i]:
                    start = mid
                else:
                    end = mid

            if result[start] >= nums[i]:
                result[start] = nums[i]
                insert_at = start
            else:
                result[end] = nums[i]
                insert_at = end

            if insert_at == res_len:
                res_len += 1

        return res_len
