# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.queue = []

    # beats 56.25%
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        tmpN = n
        ans = 0
        while tmpN > 0:
            tmpBuf = ['']*4
            read4(tmpBuf)
            self.queue += tmpBuf # same as self.queue.extend(tmpBuf)
            read_len = min(len(self.queue), n-ans)
            for i in xrange(read_len):
                buf[ans+i] = self.queue.pop(0) # from the first element

            tmpN -= read_len
            ans += read_len

            if read_len < 4:
                break

        return ans