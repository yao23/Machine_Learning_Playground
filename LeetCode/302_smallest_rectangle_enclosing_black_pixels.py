class Solution(object):
    # beats 73.33%
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x + 1, len(image), False)
        left = self.searchColumns(image, 0, y, top, bottom, True)
        right = self.searchColumns(image, y + 1, len(image[0]), top, bottom, False)
        return (right - left) * (bottom - top)

    def searchRows(self, image, i, j, opt):
        while i != j:
            m = (i + j) / 2
            if ('1' in image[m]) == opt:
                j = m
            else:
                i = m + 1
        return i

    def searchColumns(self, image, i, j, top, bottom, opt):
        while i != j:
            m = (i + j) / 2
            if any(image[k][m] == '1' for k in xrange(top, bottom)) == opt:
                j = m
            else:
                i = m + 1
        return i