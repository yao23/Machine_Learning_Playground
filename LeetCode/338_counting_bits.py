class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]

        beats 94.38%
        """
        ini_arr = [0]
        if num > 0:
            while len(ini_arr) < num + 1:
                ini_arr.extend([x + 1 for x in ini_arr])

        return ini_arr[0:num + 1]
