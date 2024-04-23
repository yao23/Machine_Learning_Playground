class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        https://www.youtube.com/watch?v=gqXU1UyA8pk

        beats 89.85%
        """
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k: # windowLength - frequencyOfMostAppearedLetter, replace others instead of most appeared one (at most k times), so move left point to shrink window
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)

    def characterReplacementV0(self, s: str, k: int) -> int:
        """
        beats 29.75%
        """
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k: # windowLength - frequencyOfMostAppearedLetter, replace others instead of most appeared one (at most k times)
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

