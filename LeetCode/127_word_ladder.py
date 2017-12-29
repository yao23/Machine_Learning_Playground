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

        def bfs_helper(start, end, word_dic):
            step = 0
            visited_set = set()
            start_set = set()
            end_set = set()
            start_set.add(start)
            end_set.add(end)
            visited_set.add(start)
            visited_set.add(end)

            while start_set and end_set:
                step += 1
                # always start from smaller set
                if len(start_set) > len(end_set):
                    tmp_set = start_set
                    start_set = end_set
                    end_set = tmp_set

                next_set = set()
                for word in start_set:
                    for idx, letter in enumerate(word):
                        tmp_str = word[:idx] + "_" + word[idx + 1:]
                        dic_word = word_dic.get(tmp_str)
                        if dic_word in end_set:
                            return step + 1
                        else:
                            if tmp_str in word_dic and dic_word not in visited_set:
                                next_set.add(dic_word)
                                visited_set.add(dic_word)
                start_set = next_set

            return step

        if endWord not in wordList:
            return 0
        else:
            word_dict = construct_graph(wordList)
            return bfs_helper(beginWord, endWord, word_dict)

    def ladderLength2(self, beginWord, endWord, wordList):
        """
        two-end BFS

        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        if endWord not in wordList:
            return 0

        begin_set, end_set = set([beginWord]), set([endWord])
        wordSet = set(wordList)

        length = 1
        alphabets = list(map(chr, range(ord('a'), ord('z') + 1)))

        while begin_set:
            # find all possible one-change words in the wordList
            begin_set = wordSet & set(
                word[:idx] + char + word[idx + 1:] for word in begin_set for idx in range(len(beginWord)) for char in
                alphabets)

            if begin_set & end_set:
                # if there are common word in next_level and end_set
                return length + 1

            length += 1

            # always proceed on the smaller set
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            # remove from wordList all the visted words in next_level, so as to avoid revisiting
            wordSet -= begin_set

        return 0
