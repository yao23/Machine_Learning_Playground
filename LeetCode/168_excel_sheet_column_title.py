class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str

        beats 46.90%
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1) % 26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
