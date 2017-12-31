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
        if endWord not in wordList:
            return []
        self.visited = {}
        self.tree = collections.defaultdict(set)
        self.beginWord = beginWord
        self.endWord = endWord
        self.wordList = wordList

        def addPath(tree, start, end, is_forward):
            if is_forward:
                tree[start].add(end)
            else:
                tree[end].add(start)

        def preprocess(wordList):
            # For each possible form of a word, find its relatives.
            word_map = collections.defaultdict(set)
            for word in wordList:
                for i in range(len(word)):
                    match_one_letter = word[0:i] + "_" + word[i+1:]
                    word_map[match_one_letter].add(word)
            return word_map

        self.word_map = preprocess(wordList)

        def getNeighbors(word):
            # Reduce O(w) time to constant time for get_neighbors.
            result = []
            for i in range(len(word)):
                match_one_letter = word[0:i] + "_" + word[i+1:]
                for match in self.word_map[match_one_letter]:
                    if match not in self.visited and match != word:
                        result.append(match)
            return set(result)

        def bibfs(cur_level, other_level, is_forward):
            if len(cur_level) == 0:  # Nothing to find...
                return False
            if len(cur_level) > len(other_level):
                return bibfs(other_level, cur_level, not is_forward)
            next_level = []
            done = False
            for node in cur_level:
                self.visited[node] = True
                for neighbor in getNeighbors(node):
                    if neighbor not in cur_level:  # Rejects longer path.
                        addPath(self.tree, node, neighbor, is_forward)
                    if neighbor in other_level:  # Found
                        done = True
                    next_level.append(neighbor)
            # Finish adding nodes...
            return done or bibfs(next_level, other_level, is_forward)

        def constructPath(begin_word, end_word, tree):
            if begin_word == end_word:
                return [[begin_word]]
            return [[begin_word] + path for next_word in tree[begin_word]
                    for path in constructPath(next_word, end_word, tree)]

        found = bibfs([beginWord], [endWord], True)
        if found:
            return constructPath(beginWord, endWord, self.tree)
        else:
            return []
