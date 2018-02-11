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

    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87799/Python-56ms-solution

        beats 63.47%
        """
        if len(s) < k:
            return 0
        my_dict, my_set = {}, set()
        for c in s:
            if c in my_dict.keys():
                my_dict[c] += 1
            else:
                my_dict[c] = 1
            if my_dict[c] >= k:
                my_set.discard(c)
            else:
                my_set.add(c)
        if len(my_set) == 0:
            return len(s)
        intervals, start = [], 0
        while start < len(s):
            if s[start] not in my_set:
                i = start
                while start < len(s):
                    if s[start] not in my_set:
                        start += 1
                    else:
                        break
                intervals.append((i, start))
            else:
                start += 1
        g_max = 0
        for interval in intervals:
            g_max = max(g_max, self.longestSubstring(s[interval[0]:interval[1]], k))
        return g_max

    def longestSubstring3(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/111914/python-solution-beats-95

        beats 37.44%
        """
        if len(s) < k:
            return 0
        if s == "":
            return 0

        dic = {}

        for i in s:
            dic[i] = dic.get(i, 0) + 1

        bad_chars = []
        for c, v in dic.items():
            if v < k:
                bad_chars.append(c)
        if len(bad_chars) == 0:
            return len(s)

        max_s = 0
        start = 0
        for i in range(len(s)):
            if s[i] in bad_chars:
                max_s = max(max_s, self.longestSubstring(s[start:i], k))
                start = i + 1

        max_s = max(max_s, self.longestSubstring(s[start:], k))
        return max_s
