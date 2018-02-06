class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        beats 79.58%
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

    def combinationSum2_1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Backtracking solution
        beats 48.05%
        """

        def dfs(candidates, target, depth, tmp_res, res):
            if target < 0:
                return
            elif target == 0:
                res.append(list(tmp_res))
            else:
                length = len(candidates)
                i = depth
                while i < length:
                    dfs(candidates, target - candidates[i], i + 1, tmp_res + [candidates[i]], res)
                    i += 1
                    while 0 < i < length and candidates[i - 1] == candidates[i]:
                        i += 1

        res = []
        if candidates:
            candidates.sort()
            dfs(candidates, target, 0, [], res)
            return res
        else:
            return res
