class Solution:
    def minFlips(self, s: str) -> int:
        """
        https://www.youtube.com/watch?v=MOeuK6gaC2A&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=8

        111000111000
        010101
        101010
        
        beats 39.95%
        """
        n = len(s)
        s = s + s # trick to make double length of origin string for easy comparing
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"

        res = len(s)
        diff1, diff2 = 0, 0
        l = 0 # sliding window
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            if (r - l + 1) > n: # enter 2nd same half of the string 
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            
            if (r - l + 1) == n: # cover the original string length
                res = min(res, diff1, diff2)
        return res
