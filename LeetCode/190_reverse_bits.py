class Solution:
    # @param n, an integer
    # @return an integer
    # beats 86.13%
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)