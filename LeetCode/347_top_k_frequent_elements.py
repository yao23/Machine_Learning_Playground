import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Use Counter to extract the top k frequent elements
        most_common(k) return a list of tuples, where the first item of the tuple is the element,
        and the second item of the tuple is the count
        Thus, the built-in zip function could be used to extract the first item from the tuples

        similar: LC 692

        beats 71.68%
        """
        return zip(*collections.Counter(nums).most_common(k))[0]

    def topKFrequent1(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        dictionary + min heap

        beats 71.68%
        """
        freq = {}
        freq_list = []
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        for key in freq.keys():
            freq_list.append((-freq[key], key))  # -freq[key] is easier for sorting when heapify
        heapq.heapify(freq_list)
        top_k = []
        for i in range(0, k):
            top_k.append(heapq.heappop(freq_list)[1])
        return top_k

    def topKFrequent2(nums, k):
        """
        :param k:
        :return:

        dictionary + quick select

        beats 63.71%
        """
        def quick_select(left, right):
            pivot = left
            l, r = left, right
            while l < r:
                while l < r and counts[r][1] <= counts[pivot][1]:
                    r -= 1
                while l < r and counts[l][1] >= counts[pivot][1]:
                    l += 1
                counts[l], counts[r] = counts[r], counts[l]
            counts[left], counts[l] = counts[l], counts[left]

            if l + 1 == k:
                return counts[:l + 1]
            elif l + 1 < k:  # right half
                return quick_select(l + 1, right)
            else:  # left half
                return quick_select(left, l - 1)

        if not nums:
            return []

        # Get the counts.
        counts = {}
        for x in nums:
            counts[x] = counts.setdefault(x, 0) + 1

        counts = counts.items()
        # Use quick select to get the top k counts.
        return [c[0] for c in quick_select(0, len(counts) - 1)]

    def topKFrequent3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        beats 31.81%
        """
        c = collections.Counter(nums)
        return heapq.nlargest(k, c, c.get)
