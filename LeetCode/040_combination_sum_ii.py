class Solution(object):
    # beats 79.58%
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])