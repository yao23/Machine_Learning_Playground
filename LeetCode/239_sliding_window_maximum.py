import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        use two-end queue to store max number index in current window
        pop out smaller ones if current number is larger
        pop left number index in two-end queue if it slides out of window
        store two-end queue first number in result list as maximum sliding window number

        beats 43.88%
        """
        two_end_queue = collections.deque()
        res_list = []
        for i, num in enumerate(nums):
            while two_end_queue and nums[two_end_queue[-1]] < num:
                two_end_queue.pop()
            two_end_queue += i,
            if two_end_queue[0] == i - k:
                two_end_queue.popleft()
            if i >= k - 1:
                res_list += nums[two_end_queue[0]],
        return res_list
