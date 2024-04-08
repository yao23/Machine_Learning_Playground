class Solution:
    def reverseBits(self, n: int) -> int:
        """
        https://www.youtube.com/watch?v=UcoN6UjAI64

        beats 39.41%
        """
        res = 0
        maxLen = 32
        for i in range(maxLen):
            bit = (n >> i) & 1 # get most right bit
            res += (bit << (maxLen - 1 - i)) # move bit to the left position
        return res
    
        # res = 0
        # for i in range(32):
        #     bit = (n >> i) & 1
        #     res += (bit << (31 - i))
        # return res
    
    def reverseBitsV0(self, n):
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
