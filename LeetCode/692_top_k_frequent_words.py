import collections
import heapq
import functools


@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # beats 43.06%
        counts = collections.Counter(words)

        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))  # (Element(count, word), word) tuple sorted by Element
            if len(freqs) > k:
                heapq.heappop(freqs)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]

    def topKFrequent1(self, words, k):
        # beats 77.28%
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1

        ret = sorted(d, key=lambda word: (-d[word], word))

        return ret[:k]