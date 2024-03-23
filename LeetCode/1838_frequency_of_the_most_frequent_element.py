class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        https://www.youtube.com/watch?v=vgBrQ0NM5vE&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=8
    
        beats 48.90%
        """
        nums.sort()
        l, r = 0, 0
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k: # over allowed increment, mathmetical thinking and modeling
                total -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res
