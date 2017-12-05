class Solution(object):
    # beats 98.70%
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def hits(grid):
            return [[h
                     for block in ''.join(row).split('W')
                     for h in [block.count('E')] * len(block) + [0]]
                    for row in grid]
        rowhits = hits(grid)
        colhits = zip(*hits(zip(*grid)))
        return max([rh + ch
                    for row in zip(grid, rowhits, colhits)
                    for cell, rh, ch in zip(*row)
                    if cell == '0'] or [0])