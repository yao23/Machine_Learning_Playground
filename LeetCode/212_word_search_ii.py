class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # moving to children
        cur.isWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]

        beats 31.72%

        https://www.youtube.com/watch?v=asbcE9mZz_U&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=14
        """
        root = TrieNode()
        for w in words:
            root.addWord(w)

        row, col = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == row or c == col or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))

        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
                
        return list(res)
    
    
    def findWords0(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]

        beats 81.75%
        """
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '')
        return list(self.res)

    def find(self, board, i, j, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.find(board, i + 1, j, trie[board[i][j]], pre + board[i][j])
            self.find(board, i, j + 1, trie[board[i][j]], pre + board[i][j])
            self.find(board, i - 1, j, trie[board[i][j]], pre + board[i][j])
            self.find(board, i, j - 1, trie[board[i][j]], pre + board[i][j])
            self.used[i][j] = False
