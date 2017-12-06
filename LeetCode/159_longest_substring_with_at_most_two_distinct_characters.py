class Solution(object):
    # beats 25.80%
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        distinct = {}  # char: pos
        maxlen = 0
        left = 0

        for right, char in enumerate(s):
            if len(distinct) == 2 and char not in distinct:
                left = min(distinct.values()) + 1
                self.remove_lowest_char(distinct)
            distinct[char] = right
            maxlen = max(maxlen, right - left + 1)
        return maxlen

    def remove_lowest_char(self, distinct):
        lowest_pos = min(distinct.values())
        for k, pos in distinct.items():
            if pos == lowest_pos:
                char = k
        distinct.pop(char)