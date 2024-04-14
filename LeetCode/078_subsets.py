class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        https://www.youtube.com/watch?v=REOH22Xwdkk
        
        beats 51.05%
        """
        res = []

        def dfs(depth, tmp):
            if depth == len(nums):
                res.append(tmp.copy())
                return

            # decision to not include current number
            dfs(depth + 1, tmp)

            # decision to include current number
            tmp.append(nums[depth])
            dfs(depth + 1, tmp)
            tmp.pop()

        dfs(0, [])
        return res
        
    def subsetsV0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Iterative
        beats 59.50%
        """
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    def subsets1(self, nums):
        """
        :param nums:
        :return:

        DFS recursively
        beats 16.57%
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def subsets2(self, nums):
        """
        :param nums:
        :return:

        Bit Manipulation
        """
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
