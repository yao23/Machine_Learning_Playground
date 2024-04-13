class Solution(object):
    """
    https://www.youtube.com/watch?v=P6RZZMu_maU

    beats 24.02%
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        for n in nums:
            if (n - 1) not in s: # check its the start of a sequence
                length = 0
                while (n + length) in s:
                    length += 1
                res = max(res, length)
        return res
        
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        @param num, a list of integer
        @return an integer
        beats 77.49%
        """
        nums = set(nums)
        max_len = 0
        while nums:
            n = nums.pop()
            i = n+1
            l1 = 0
            l2 = 0
            while i in nums:
                nums.remove(i)
                i += 1
                l1 += 1
            i = n - 1
            while i in nums:
                nums.remove(i)
                i -= 1
                l2 += 1
            max_len = max(max_len, l1 + l2 + 1)
        return max_len
