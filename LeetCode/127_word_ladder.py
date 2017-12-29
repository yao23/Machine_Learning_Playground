from collections import deque


class Solution(object):
    # beats 68.80%
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        use underscore to replace each character in the wordList to save time than replace with letters from a to z

        """

        def construct_dict(word_list):
            dict_word = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    dict_word[s] = dict_word.get(s, []) + [word]
            return dict_word

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        dict_words = construct_dict(set(wordList))
        return bfs_words(beginWord, endWord, dict_words)
