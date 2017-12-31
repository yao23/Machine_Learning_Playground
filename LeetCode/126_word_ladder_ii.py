import collections


class Solution(object):
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    # beats 84.21%
    # https://discuss.leetcode.com/topic/112221/clear-and-modular-solution-of-python-beats-90
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        def add_path(tree, start, end, is_forward):
            if is_forward:
                tree[start].add(end)
            else:
                tree[end].add(start)

        def preprocess(words_list):
            # For each possible form of a word, find its relatives.
            word_map = collections.defaultdict(set)
            for word in words_list:
                for i in range(len(word)):
                    match_one_letter = word[0:i] + "_" + word[i+1:]
                    word_map[match_one_letter].add(word)
            return word_map

        def get_neighbors(word):
            # Reduce O(w) time to constant time for get_neighbors.
            result = []
            for i in range(len(word)):
                match_one_letter = word[0:i] + "_" + word[i+1:]
                for match in self.word_map[match_one_letter]:
                    if match not in self.visited and match != word:
                        result.append(match)
            return set(result)

        def bi_bfs(cur_level, other_level, is_forward):
            if len(cur_level) == 0:  # Nothing to find...
                return False
            if len(cur_level) > len(other_level):
                return bi_bfs(other_level, cur_level, not is_forward)
            next_level = []
            done = False
            for node in cur_level:
                self.visited[node] = True
                for neighbor in get_neighbors(node):
                    if neighbor not in cur_level:  # Rejects longer path.
                        add_path(self.tree, node, neighbor, is_forward)
                    if neighbor in other_level:  # Found
                        done = True
                    next_level.append(neighbor)
            # Finish adding nodes...
            return done or bi_bfs(next_level, other_level, is_forward)

        def construct_path(begin_word, end_word, tree):
            if begin_word == end_word:
                return [[begin_word]]
            return [[begin_word] + path for next_word in tree[begin_word]
                    for path in construct_path(next_word, end_word, tree)]

        if endWord not in wordList:
            return []
        self.visited = {}
        self.tree = collections.defaultdict(set)
        self.begin_word = beginWord
        self.end_word = endWord
        self.word_list = wordList
        self.word_map = preprocess(wordList)

        found = bi_bfs([beginWord], [endWord], True)  # bi-direction BFS
        if found:
            return construct_path(beginWord, endWord, self.tree)
        else:
            return []

    def findLadders1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]

        https://leetcode.com/submissions/detail/134036243/
        It maintains a dictionary(called parent) which has:
        key: "next step string"
        value: set of "current string"s
        For example, 'cog': set(['dog', 'log']). Both 'dog' and 'log' can be transformed to 'cog'.

        "hit"
        "cog"
        ["hot","dot","dog","lot","log","cog"]
        parents: defaultdict(<class 'set'>, {'cog': {'dog', 'log'}, 'dog': {'dot'}, 'log': {'lot'},
                                'lot': {'hot'}, 'dot': {'hot'}, 'hot': {'hit'}})

        Then it went through the dictionary to get the path.

        beats 49.02%
        """
        word_set = set([])
        for word in wordList:
            word_set.add(word)

        level = set([beginWord])

        parents = collections.defaultdict(set)

        while level and endWord not in parents:  # BFS
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    p1 = word[:i]
                    p2 = word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        # accelerate
                        if word[i] != j:
                            child_word = p1 + j + p2
                            if child_word in word_set and child_word not in parents:
                                next_level[child_word].add(word)
            level = next_level
            parents.update(next_level)

        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
