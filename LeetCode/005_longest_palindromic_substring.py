class Solution(object):
    # @return a string
    # beats 98.77%
    def longestPalindrome(self, s):
        """
		:type s: str
		:rtype: str
		"""
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in xrange(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]

# Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2,
# and that new maxPalindrome includes this new character. Proof: if on adding 1 character,
# maxPalindromeLen increased by 3 or more, say the new maxPalindromeLen is Q, and the old maxPalindromeLen is P,
# and Q>=P+3. Then it would mean, even without this new character, there would be a palindromic substring ending
# in the last character, whose length is at least Q-2. Since Q-2 would be >P, this contradicts the condition that
# P is the maxPalindromeLen without the additional character.

# So, it becomes simple, you only need to scan from beginning to the end, adding one character at a time,
# keeping track of maxPalindromeLen, and for each added character, you check if the substrings ending with
# this new character, with length P+1 or P+2, are palindromes, and update accordingly.
