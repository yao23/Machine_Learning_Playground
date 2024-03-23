class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        https://www.youtube.com/watch?v=wiGpQwVHdE0&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=2
        
        beats 55.84%
        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        
    def lengthOfLongestSubstringV0(self, s):
        """
        :type s: str
        :rtype: int

        if meet duplicate character and move start pointer to the index after previously appeared one
        otherwise calculate max length

        beats 86.09%
        """
        start = max_length = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_char[s[i]] = i

        return max_length
