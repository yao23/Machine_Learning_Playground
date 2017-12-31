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

        def addPath(tree, start, end, isForward):
            if isForward:
                tree[start].add(end)
            else:
                tree[end].add(start)

        def preprocess(wordList):
            # For each possible form of a word, find its relatives.
            wordMap = collections.defaultdict(set)
            for word in wordList:
                for i in range(len(word)):
                    matchOneLetter = word[0:i] + "_" + word[i+1:]
                    wordMap[matchOneLetter].add(word)
            return wordMap

        self.wordMap = preprocess(wordList)

        def getNeighbors(word):
            # Reduce O(w) time to constant time for get_neighbors.
            result = []
            for i in range(len(word)):
                matchOneLetter = word[0:i] + "_" + word[i+1:]
                for match in self.wordMap[matchOneLetter]:
                    if match not in self.visited and match != word:
                        result.append(match)
            return set(result)


        def bibfs(thislev, otherlev, isForward):
            if len(thislev) == 0: # Nothing to find...
                return False
            if len(thislev) > len(otherlev):
                return bibfs(otherlev, thislev, not isForward)
            nextlev = []
            done = False
            for node in thislev:
                self.visited[node] = True
                for neighbor in getNeighbors(node):
                    if neighbor not in thislev: # Rejects longer path.
                        addPath(self.tree, node, neighbor, isForward)
                    if neighbor in otherlev: # Found
                        done = True
                    nextlev.append(neighbor)
            # Finish adding nodes...
            return done or bibfs(nextlev, otherlev, isForward)


        def constructPath(beginWord, endWord, tree):
            if beginWord == endWord:
                return [[beginWord]]
            return [[beginWord] + path for nextWord in tree[beginWord] for path in constructPath(nextWord, endWord, tree)]

        found = bibfs([beginWord], [endWord], True)
        if found:
            return constructPath(beginWord, endWord, self.tree)
        else:
            return []
