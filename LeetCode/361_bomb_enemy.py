class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        beats 98.70%
        """
        def hits(grid):
            return [[h
                     for block in ''.join(row).split('W')
                     for h in [block.count('E')] * len(block) + [0]]
                    for row in grid]
        row_hits = hits(grid)
        col_hits = zip(*hits(zip(*grid)))
        return max([rh + ch
                    for row in zip(grid, row_hits, col_hits)
                    for cell, rh, ch in zip(*row)
                    if cell == '0'] or [0])
