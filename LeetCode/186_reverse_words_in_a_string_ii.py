class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.

        beats 27.10%
        """
        str.reverse()

        index = 0
        for i in range(len(str)):
            if str[i] == " ":
                str[index: i] = reversed(str[index: i])
                index = i + 1

        str[index: ] = reversed(str[index: ])
