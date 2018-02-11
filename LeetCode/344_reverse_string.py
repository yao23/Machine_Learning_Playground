class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        https://leetcode.com/problems/reverse-string/discuss/80946/Python-(3-solutions:-Recursive-Classic-Pythonic)

        beats 51.55%
        """
        return s[::-1]

    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str

        left, right pointers

        beats 19.20%
        """
        char_arr = list(s)
        left, right = 0, len(char_arr) - 1
        while left < right:
            char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
            left += 1
            right -= 1

        return "".join(char_arr)

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str

        recursive
        beats 1.97%
        """
        str_len = len(s)
        if str_len < 2:
            return s
        return self.reverseString(s[str_len / 2:]) + self.reverseString(s[:str_len / 2])
