class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2,
        and that new maxPalindrome includes this new character. Proof: if on adding 1 character,
        maxPalindromeLen increased by 3 or more, say the new maxPalindromeLen is Q, and the old maxPalindromeLen is P,
        and Q>=P+3. Then it would mean, even without this new character, there would be a palindromic substring ending
        in the last character, whose length is at least Q-2 (remove 1 character for odd length string or 2 for odd/even
        length string and the rest string whose length is Q-1 or Q-2 is still palindromic, Q-1 or Q-2 is still larger
        than P). Since Q-2 would be >P, this contradicts the condition that P is the maxPalindromeLen without the
        additional character.

        So, it becomes simple, you only need to scan from beginning to the end, adding one character at a time,
        keeping track of maxPalindromeLen, and for each added character, you check if the substrings ending with
        this new character, with length P+1 or P+2, are palindromes, and update accordingly.

        beats 98.77%

        """
        if len(s) == 0:
            return 0
        max_len = 1
        start = 0
        for i in range(len(s)):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue

            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]
