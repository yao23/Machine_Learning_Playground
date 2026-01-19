class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        n = row * col
        l, r = 0, n - 1
        while l <= r:
            mid = (r - l) // 2 + l
            mNum = matrix[mid // col][mid % col]
            if mNum == target:
                return True
            elif mNum < target:
                l += 1
            else:
                r -= 1
        return False
