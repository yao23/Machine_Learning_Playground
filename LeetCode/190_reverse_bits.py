class Solution:
    def reverseBits(self, n):
        """
        :param n:
        :return:
        @param n, an integer
        @return an integer

        beats 86.13%
        """
        ori_bin = '{0:032b}'.format(n)
        reverse_bin = ori_bin[::-1]
        return int(reverse_bin, 2)
