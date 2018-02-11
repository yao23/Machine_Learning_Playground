class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python

        If every character appears at least k times, the whole string is ok. Otherwise split by a least frequent
        character (because it will always be too infrequent and thus can't be part of any ok substring) and make the
        most out of the splits.

        beats 45.66%
        """
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))

    def longestSubstring1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        take the first too rare character instead of a rarest

        beats 51.60%
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)