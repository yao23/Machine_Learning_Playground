class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        https://www.youtube.com/watch?v=GBKI9VSKdGg
        
        beats 71.12%
        """
        res = []

        def dfs(depth, tmp, sum):
            if sum == target:
                res.append(tmp.copy())
                return
            if depth == len(candidates) or sum > target:
                return

            tmp.append(candidates[depth])
            dfs(depth, tmp, sum + candidates[depth])
            tmp.pop()

            dfs(depth + 1, tmp, sum)

        dfs(0, [], 0)
        return res
        
    def combinationSumV0(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        beats 42.88%
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)
