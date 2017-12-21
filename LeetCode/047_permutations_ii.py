class Solution(object):
    # beats 95.68%
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [1,2,3]
        # [[1]] => [[2,1],[1,2]] => [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break              # handles duplication
            ans = new_ans
        return ans
