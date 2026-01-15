class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, j in enumerate(nums):
            if (target - j) in dic:
                return [dic[target - j], i]
            else:
                dic[j] = i
