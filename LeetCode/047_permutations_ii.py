import collections

class Solution(object):
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        https://www.youtube.com/watch?v=qhBVWf0YafA
        
        beats 87.52%
        """
        result = []
        counter = collections.Counter(nums)

        def backtrack(perm, counter):
            if len(perm) == len(nums):
                result.append(perm.copy())

            for n in counter:
                if counter[n] == 0:
                    continue
                perm.append(n)
                counter[n] -= 1
                backtrack(perm, counter)
                perm.pop()
                counter[n] += 1

        backtrack([], counter)

        return result

    def helper_method(self, nums, nums_len, depth, result):
        if depth == nums_len:
            tmp_res = list(nums)
            result.append(tmp_res)
            return

        nums_set = []  # remove duplicate
        for i in range(depth, nums_len):
            if nums[i] in nums_set:
                continue
            else:
                nums_set.append(nums[i])
                if depth == i:
                    self.helper_method(nums, nums_len, depth + 1, result)
                else:
                    nums[depth], nums[i] = nums[i], nums[depth]
                    self.helper_method(nums, nums_len, depth + 1, result)
                    nums[depth], nums[i] = nums[i], nums[depth]

    def permuteUnique1(self, nums):
        """
        :param nums:
        :return:

        beats 75.12%
        """
        result = []
        nums_len = len(nums)
        sorted(nums)
        self.helper_method(nums, nums_len, 0, result)
        return result

    def permuteUniqueV0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        [1,2,3]
        [[1]] => [[2,1],[1,2]] => [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]

        beats 95.68%
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break  # handles duplication
            ans = new_ans
        return ans

