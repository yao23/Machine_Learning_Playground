class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        check every index in the current available range to reach the end or not

        beats 44.25%
        """
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            max_end = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end
        return step

    def jump1(self, nums):
        """
        :param nums:
        :return:

        check indices before each index from 1 to nums_len - 1
        stop at the leftmost one which enables jump from j to i

        time: O(n), space: O(n)

        beats 55.00%
        """
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        min_step = [0] * nums_len
        min_step[0] = 0
        cur_index = 0

        for i in range(1, nums_len):
            for j in range(cur_index, i):
                if nums[j] + j >= i:
                    min_step[i] = min_step[j] + 1
                    cur_index = j
                    break  # stop at the leftmost one

        return min_step[-1]
