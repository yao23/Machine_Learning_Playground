# The read4 API is already defined for you.
def read4(buf):
    """
    :param buf: a list of characters
    :return: an integer
    """
    pass


class Solution(object):
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)

        beats 56.25%
        """
        tmpN = n
        ans = 0
        while tmpN > 0:
            tmpBuf = ['']*4
            read4(tmpBuf)
            self.queue += tmpBuf # same as self.queue.extend(tmpBuf)
            read_len = min(len(self.queue), n-ans)
            for i in xrange(read_len):
                buf[ans+i] = self.queue.pop(0)  # from the first element

            tmpN -= read_len
            ans += read_len

            if read_len < 4:
                break

        return ans
