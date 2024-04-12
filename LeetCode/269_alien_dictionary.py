import collections


class Solution(object):
    def alienOrder(self, words: List[str]) -> str:
        """
        https://www.youtube.com/watch?v=6kTZYvNNyps
        """
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

    def alienOrderV0(self, words):
        """
        :type words: List[str]
        :rtype: str

        beats 33.84%
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

    def alienOrder1(self, words):
        """
        :type words: List[str]
        :rtype: str

        similar like 210 Course Schedule II

        beats 10.85%
        """
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        free = chars - set(pre)  # nodes without pre
        order = ''
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)
