class Solution(object):
    """
    https://www.youtube.com/watch?v=XYQecbcd6_c
    
    expand from middle to left and right to find longest palindrome substring
    
    beats 63.02%
    """
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i  
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

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

        if input string is infinite, it wants to get longest palindrome substring so far, the idea is to use an array
        with size 26, which records the current longest palindrome substring could be ended in that letter.
        for example, for input string "zaaa" which could be ended by "a" or "z" for next possible longest palindrome
        substring, so arr[0] = "zaaa", arr[25] = "zaaa", iterate the array and get longest one then trim first letter
        ("z" in the example), then we can get longest palindrome substring so far.

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
