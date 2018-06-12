import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        beats 5.81%
        """
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    def partition(self, nums, l, r):
        """
        :param nums:
        :param l:
        :param r:
        :return:

        choose the right-most element as pivot
        """
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def findKthLargest1(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        O(nlgn) time
        """
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest2(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        O(nk) time, bubble sort idea, TLE
        """
        for i in xrange(k):
            for j in xrange(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[len(nums) - k]

    def findKthLargest3(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        O(nk) time, selection sort idea
        """
        for i in xrange(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in xrange(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]

    def findKthLargest4(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        O(k+(n-k)lgk) time, min-heap
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in xrange(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    def findKthLargest5(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        O(k+(n-k)lgk) time, min-heap
        """
        return heapq.nlargest(k, nums)[k - 1]
