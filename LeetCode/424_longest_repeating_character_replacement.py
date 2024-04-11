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

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
