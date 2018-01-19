class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration/8

        1. there are no elements that appears more than n/3 times, then whatever the algorithm got from 1st round
        wound be rejected in the second round.
        2. there are only one elements that appears more than n/3 times, after 1st round one of the candidate must be
        that appears more than n/3 times(<2n/3 other elements could only pair out for <n/3 times), the other candidate
        is not necessarily be the second most frequent but it would be rejected in 2nd round.
        3. there are two elments appears more than n/3 times, candidates would contain both of them. (<n/3 other
        elements couldn't pair out any of the majorities.)

        beats 58.89%
        """
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
