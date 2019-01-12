class Solution(object):
    def countOne(self, num):
        count = 0
        for i in xrange(8):
            if num >> (7 - i) & 1 == 1:
                count += 1
            else:
                break
        return count

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool

        # beats 32.31%
        """
        n = len(data)
        ind = 0
        while ind < n:
            m = self.countOne(data[ind])
            if ind + m > n:
                return False
            if m == 0:
                if (data[ind] >> 7) & 1 != 0:
                    return False
            elif m == 1 or m > 4:
                return False
            else:
                for i in xrange(m):
                    if (data[ind] >> (7 - i)) & 1 != 1:
                        return False
                if (data[ind] >> (7 - i - 1)) & 1 != 0:
                    return False
                for i in xrange(ind + 1, ind + m):
                    if (data[i] >> 7) & 1 != 1:
                        return False
                    if (data[i] >> 6) & 1 != 0:
                        return False
            ind += m
            if m == 0:
                ind += 1
        return True
