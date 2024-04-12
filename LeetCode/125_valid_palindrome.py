class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        beats 40.95%
        """
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isPalindromeV1(self, s: str) -> bool:
        """
        https://www.youtube.com/watch?v=jJXJ16kPFWg
        
        beats 91.26%
        """
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])

    def isPalindromeV0(self, s: str) -> bool:
        """
        beats 12.72%
        """
        def isAlphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
