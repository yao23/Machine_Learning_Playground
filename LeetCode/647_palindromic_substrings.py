class Solution:
    """
    beats 12.01%
    """
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                curStr = s[i:j]
                if curStr == curStr[::-1]:
                    res += 1
        return res
