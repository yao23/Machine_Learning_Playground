import collections


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/degree-of-an-array/discuss/108666/Python-easy-and-concise-solution

        beats 36.06%
        """
        c = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)

    def findShortestSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/degree-of-an-array/discuss/108647/Python-O(n)-concise-with-explanation-(two-approaches)

        Firstly, group each num and collect the index it appears into a list. The list with the longest length will be
        the degree of the array.

        Next loop through each of the lists, only those lists with the same length as the degree will qualify.
        We simply take difference between the first and last value of each qualifying lists to find the length of such
        a possible subarray.

        For example if we have [1, 1, 2, 2, 2, 3, 1], after grouping by value:

        [1, 1, 2, 2, 2, 3, 1] => { 1: [0, 1, 6], 2: [2, 3, 4], 3: [4] }, degree: 3

        Only have to consider values where the length == degree:

        1: [0, 1, 6] => subarray length: (6 - 0) + 1 = 7
        2: [2, 3, 4] => subarray length: (4 - 2) + 1 = 3 (Winner!)

        beats 27.26%
        """
        nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            deg = max(deg, len(nums_map[num]))
        for num, indices in nums_map.items():
            if len(indices) == deg:
                min_len = min(min_len, indices[-1] - indices[0] + 1)
        return min_len

    def findShortestSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        beats 52.72%
        """
        nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            if len(nums_map[num]) == deg:
                min_len = min(min_len, nums_map[num][-1] - nums_map[num][0] + 1)
            elif len(nums_map[num]) > deg:
                deg = len(nums_map[num])
                min_len = nums_map[num][-1] - nums_map[num][0] + 1
        return min_len
