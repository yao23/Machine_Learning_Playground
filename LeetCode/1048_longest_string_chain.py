class Solution:
    """
    https://www.youtube.com/watch?v=7b0V1gT_TIk

    Input: words = ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: b => ba => bca / bda => bdca
    
    beats 62.18%
    """
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w : -len(w)) # sort words from longest to shortest
        dp = {}
        wordIndex = {} # map word to index
        for i, w in enumerate(words):
            wordIndex[w] = i

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1

            for j in range(len(words[i])): # go over each character in current word
                cur = words[i]
                pred = cur[:j] + cur[j+1:] # remove current character
                if pred in wordIndex: # predecessor found
                    res = max(res,1 + dfs(wordIndex[pred])) # look for the next predessor of the current precedessor

            dp[i] = res

            return res

        for i in range(len(words)): # result may start any word in input words
            dfs(i)

        return max(dp.values()) # longest string chain
