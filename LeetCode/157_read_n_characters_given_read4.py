import math


# The read4 API is already defined for you.
def read4(buf):
    """
    :param buf: a list of characters
    :return: an integer
    """
    pass


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)

        beats 98.02%
        """
        idx = 0
        while True:
            buf4 = [""]*4
            curr = math.min(read4(buf4), n - idx)  # curr is the number of chars that reads
            for i in xrange(curr):
                buf[idx] = buf4[i]
                idx += 1
            if curr != 4 or idx == n:  # return if it reaches the end of file or reaches n
                return idx
