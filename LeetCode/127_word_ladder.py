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

    def ladderLength1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def construct_graph(word_list):
            res = {}
            for word in word_list:
                for idx, letter in enumerate(word):
                    str_replaced_letter = word[:idx] + "_" + word[idx + 1:]
                    res[str_replaced_letter] = word
            return res

        def bfs_helper(start, end, word_dict):
            step = 0
            start_set = set()
            end_set = set()
            start_set.add(start)
            end_set.add(end)

            while start_set:
                if len(start_set) > len(end_set):
                    tmp_set = start_set
                    start_set = end_set
                    end_set = tmp_set

                step += 1
                next_set = set()
                for word in start_set:
                    if word in end_set:
                        return step
                    else:
                        for idx, letter in enumerate(word):
                            tmp_str = word[:idx] + "_" + word[idx + 1:]
                            if tmp_str in word_dict:
                                next_set.add(tmp_str)
                start_set = next_set

            return step

        word_dict = construct_graph(wordList)
        return bfs_helper(beginWord, endWord, word_dict)