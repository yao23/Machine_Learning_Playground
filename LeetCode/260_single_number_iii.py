class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        beats 82.88%
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
