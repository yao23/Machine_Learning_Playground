import collections

class Solution(object):
    # beats 33.84%
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        less = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    less += a + b,
                    break
        chars = set(''.join(words))
        order = []
        while less:
            free = chars - set(zip(*less)[1])
            if not free:
                return ''
            order += free
            less = filter(free.isdisjoint, less)
            chars -= free
        return ''.join(order + list(chars))

    # beats 10.85%
    def alienOrder1(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        free = chars - set(pre)
        order = ''
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)