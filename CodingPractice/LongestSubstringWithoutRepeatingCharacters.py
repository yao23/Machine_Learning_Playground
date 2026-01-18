class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chSet:
                chSet.remove(s[l])
                l += 1

            chSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res
