class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        beats 51.55%
        """
        return s[::-1]

    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str

        beats 19.20%
        """
        char_arr = list(s)
        left, right = 0, len(char_arr) - 1
        while left < right:
            char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
            left += 1
            right -= 1

        return "".join(char_arr)
