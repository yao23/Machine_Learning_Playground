class Solution:
    """
    https://www.youtube.com/watch?v=4RACzI5-du8
    O(n^2)
    
    beats 76.04%
    """
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPalindrome(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):
            res += countPalindrome(i, i) # odd characters middle expand 
            res += countPalindrome(i, i + 1) # even characters middle expand 

        return res
        
    """
    O(n^2)
    
    beats 65.23%
    """
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:  # odd characters middle expand 
                res += 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: # even characters middle expand 
                res += 1
                l -= 1
                r += 1

        return res
        
    """
    O(n^3)
    
    beats 12.01%
    """
    def countSubstringsV0(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                curStr = s[i:j]
                if curStr == curStr[::-1]:
                    res += 1
        return res
