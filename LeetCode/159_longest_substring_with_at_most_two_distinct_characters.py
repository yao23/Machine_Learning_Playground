class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int

        beats 25.80%
        """
        distinct = {}  # char: pos
        max_len = 0
        left = 0

        for right, char in enumerate(s):
            if len(distinct) == 2 and char not in distinct:
                left = min(distinct.values()) + 1
                self.remove_lowest_char(distinct)
            distinct[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

    def remove_lowest_char(self, distinct):
        lowest_pos = min(distinct.values())
        for k, pos in distinct.items():
            if pos == lowest_pos:
                char = k
        distinct.pop(char)
